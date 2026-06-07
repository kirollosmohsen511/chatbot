"""
Hybrid Router
=============
The core "brain" of the hybrid system.
Decides which path to take for each user message:

  HIGH confidence   (≥ 0.70) → Pure Static  (fast, guaranteed)
  MEDIUM confidence (0.40–0.69) → Static + Gemini enhancement
  LOW confidence    (< 0.40) → Pure Gemini  (dynamic, flexible)

Eligibility Engine always runs on top of whatever path is chosen,
whenever the user's medical profile is available.
"""

import logging
from typing import Optional
from dataclasses import dataclass

from models.intent_classifier import IntentClassifier
from models.response_generator import get_response
from models.eligibility_engine import EligibilityEngine, DonorProfile, EligibilityResult
from models.gemini_service import GeminiService

logger = logging.getLogger(__name__)

# ── Confidence thresholds ────────────────────
HIGH_CONF   = 0.70   # Pure static
MEDIUM_CONF = 0.40   # Static + Gemini enhance


@dataclass
class HybridResult:
    reply:           str
    intent:          str
    confidence:      float
    mode:            str          # "static" | "enhanced" | "gemini" | "eligibility"
    is_eligible:     Optional[bool]  = None
    wait_days:       Optional[int]   = None
    recommendations: list            = None

    def __post_init__(self):
        if self.recommendations is None:
            self.recommendations = []


# ── Intents that always use eligibility engine when profile is present ──
ELIGIBILITY_INTENTS = {
    "eligibility_check",
    "health_conditions",
    "tattoo_piercing",
    "pregnancy",
    "age_weight",
}


class HybridRouter:
    """
    Routes each message through the best available path.
    Degrades gracefully if Gemini is unavailable.
    """

    def __init__(
        self,
        classifier:         IntentClassifier,
        eligibility_engine: EligibilityEngine,
        gemini:             Optional[GeminiService],
    ):
        self.classifier         = classifier
        self.eligibility_engine = eligibility_engine
        self.gemini             = gemini
        gemini_status = "✅ Gemini ON" if gemini else "⚠️  Gemini OFF (static only)"
        logger.info(f"HybridRouter initialized — {gemini_status}")

    # ─────────────────────────────────────────
    # Main entry point
    # ─────────────────────────────────────────

    def route(
        self,
        message:          str,
        language:         str = "ar",
        donor_profile:    Optional[DonorProfile] = None,
        history:          Optional[list] = None,
    ) -> HybridResult:
        """
        Main routing logic.

        Flow:
        1. Classify intent + confidence
        2. If eligibility intent AND profile → run eligibility engine
        3. Else based on confidence:
           HIGH   → static response
           MEDIUM → static response enhanced by Gemini
           LOW    → pure Gemini answer
        """

        # Step 1 — Classify
        clf_result = self.classifier.classify(message)
        intent     = clf_result["intent"]
        confidence = clf_result["confidence"]

        logger.info(
            f"Intent: {intent} | Confidence: {confidence:.0%} | "
            f"Lang: {language} | Gemini: {'ON' if self.gemini else 'OFF'}"
        )

        # Step 2 — Eligibility path (personalized)
        if intent in ELIGIBILITY_INTENTS and donor_profile is not None:
            return self._eligibility_path(
                message, intent, confidence, language, donor_profile
            )

        # Step 3 — Confidence-based routing
        if confidence >= HIGH_CONF or self.gemini is None:
            return self._static_path(intent, confidence, language)

        elif confidence >= MEDIUM_CONF:
            return self._enhanced_path(message, intent, confidence, language)

        else:
            return self._gemini_path(message, confidence, language, history)

    # ─────────────────────────────────────────
    # Path 1 — Pure Static
    # ─────────────────────────────────────────

    def _static_path(
        self, intent: str, confidence: float, language: str
    ) -> HybridResult:
        reply = get_response(intent, language)
        logger.info(f"Mode: STATIC | Intent: {intent}")
        return HybridResult(
            reply=reply,
            intent=intent,
            confidence=confidence,
            mode="static",
        )

    # ─────────────────────────────────────────
    # Path 2 — Static + Gemini Enhancement
    # ─────────────────────────────────────────

    def _enhanced_path(
        self, message: str, intent: str, confidence: float, language: str
    ) -> HybridResult:
        static_reply = get_response(intent, language)
        enhanced_reply = self.gemini.enhance(
            user_message=message,
            static_response=static_reply,
            language=language,
        )
        logger.info(f"Mode: ENHANCED | Intent: {intent}")
        return HybridResult(
            reply=enhanced_reply,
            intent=intent,
            confidence=confidence,
            mode="enhanced",
        )

    # ─────────────────────────────────────────
    # Path 3 — Pure Gemini
    # ─────────────────────────────────────────

    def _gemini_path(
        self,
        message:    str,
        confidence: float,
        language:   str,
        history:    Optional[list],
    ) -> HybridResult:
        reply = self.gemini.answer(
            user_message=message,
            language=language,
            conversation_history=history,
        )
        logger.info("Mode: GEMINI")
        return HybridResult(
            reply=reply,
            intent="gemini_dynamic",
            confidence=confidence,
            mode="gemini",
        )

    # ─────────────────────────────────────────
    # Path 4 — Eligibility Engine
    # ─────────────────────────────────────────

    def _eligibility_path(
        self,
        message:      str,
        intent:       str,
        confidence:   float,
        language:     str,
        profile:      DonorProfile,
    ) -> HybridResult:
        result: EligibilityResult = self.eligibility_engine.evaluate(profile)

        # Build structured reply
        reply = self._format_eligibility_reply(result, language)

        # If Gemini is available + result has nuance, enhance the reply
        if self.gemini and not result.is_eligible and result.wait_days is None:
            # Permanent disqualification — let Gemini add empathetic detail
            try:
                extra = self.gemini.enhance(
                    user_message=message,
                    static_response=reply,
                    language=language,
                )
                reply = extra
            except Exception:
                pass  # Fall back to static reply silently

        logger.info(
            f"Mode: ELIGIBILITY | Eligible: {result.is_eligible} | "
            f"Wait: {result.wait_days} days"
        )
        return HybridResult(
            reply=reply,
            intent=intent,
            confidence=confidence,
            mode="eligibility",
            is_eligible=result.is_eligible,
            wait_days=result.wait_days,
            recommendations=result.recommendations,
        )

    # ─────────────────────────────────────────
    # Helper — format eligibility reply
    # ─────────────────────────────────────────

    def _format_eligibility_reply(
        self, result: EligibilityResult, language: str
    ) -> str:
        ar = language.startswith("ar")

        if result.is_eligible:
            header = "🎉 **أنت مؤهل للتبرع بالدم!**" if ar else "🎉 **You are eligible to donate blood!**"
            checks  = "\n".join(f"  {d}" for d in result.details)
            rec_hdr = "\n\n**توصيات قبل التبرع:**" if ar else "\n\n**Before you donate:**"
            recs    = "\n".join(f"• {r}" for r in result.recommendations)
            return f"{header}\n\n{checks}{rec_hdr}\n{recs}"

        else:
            header = f"❌ **{result.reason}**" if ar else f"❌ **{result.reason_en}**"
            wait   = ""
            if result.wait_days:
                wait = (
                    f"\n\n⏳ باقي **{result.wait_days} يوم** قبل ما تتبرع."
                    if ar else
                    f"\n\n⏳ **{result.wait_days} days** remaining before you can donate."
                )
            recs = "\n".join(f"• {r}" for r in result.recommendations)
            return f"{header}{wait}\n\n{recs}"
