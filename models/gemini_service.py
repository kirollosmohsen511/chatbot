"""
Gemini Service
==============
Handles dynamic AI responses using Google Gemini API.
Only called when the static system can't handle a question well.

This is the "smart fallback" of the hybrid system.
"""

import os
import logging
from typing import Optional
import google.generativeai as genai

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# System Prompt — the "brain" of the chatbot
# This tells Gemini exactly WHO it is and HOW to behave
# ─────────────────────────────────────────────

BLOOD_DONATION_SYSTEM_PROMPT = """
أنت مساعد ذكي متخصص في منصة التبرع بالدم "Blood Donation Smart Platform".
مهمتك الوحيدة هي الإجابة على أسئلة التبرع بالدم فقط.

## هويتك:
- اسمك: مساعد منصة التبرع بالدم
- متخصص في: التبرع بالدم، بنوك الدم، الأهلية الطبية للتبرع
- تتكلم: العربية والإنجليزية (رد بنفس لغة السؤال دايماً)

## المنصة التي تخدمها:
- منصة رقمية تربط المتبرعين وطالبي الدم والمستشفيات في مصر
- تحتوي على: تطبيق موبايل (Flutter)، بوابة مستشفيات (Angular)، لوحة إدارة
- الميزات: مطابقة ذكية للمتبرعين، تنبؤ بالطلب، نظام نقاط ومكافآت، QR Code

## قواعد صارمة يجب اتباعها:
1. أجب فقط على أسئلة التبرع بالدم وصحة المتبرع
2. لو السؤال خارج نطاقك (سياسة، رياضة، ترفيه...)، قل بلطف: "أنا متخصص في التبرع بالدم فقط 🩸"
3. لا تعطِ تشخيصاً طبياً — انصح دائماً باستشارة الطبيب للحالات الصعبة
4. كن موجزاً وواضحاً — استخدم نقاط وإيموجي لتسهيل القراءة
5. معلوماتك مبنية على إرشادات منظمة الصحة العالمية WHO وبنوك الدم المصرية

## معلومات أساسية تعرفها:
- الحد الأدنى للسن: 18 سنة | الحد الأقصى: 65 سنة
- الحد الأدنى للوزن: 50 كيلوجرام
- الفترة بين التبرعات: 90 يوم للرجال، 120 يوم للسيدات
- التاتو والثقب: انتظر 6 أشهر
- الحمل والرضاعة: ممنوع التبرع
- الهيموجلوبين الأدنى: 12.5 g/dL للسيدات، 13.0 g/dL للرجال

## أسلوبك:
- ودود ومشجع على التبرع
- واضح وعلمي بدون تعقيد
- تستخدم الإيموجي باعتدال 🩸❤️✅
"""


# ─────────────────────────────────────────────
# Gemini Service Class
# ─────────────────────────────────────────────

class GeminiService:
    """
    Wraps Google Gemini API for dynamic blood donation responses.
    
    Used in two modes:
    1. ENHANCE mode  — improves a static response with more detail
    2. ANSWER mode   — answers a question the static system couldn't handle
    """

    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is not set!\n"
                "Get your free key from: https://aistudio.google.com"
            )
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",   # Free tier, fast
            system_instruction=BLOOD_DONATION_SYSTEM_PROMPT,
            generation_config=genai.GenerationConfig(
                temperature=0.4,      # Low = more consistent medical answers
                max_output_tokens=600,
            )
        )
        self.available = True
        logger.info("✅ Gemini service initialized successfully.")

    def answer(
        self,
        user_message: str,
        language: str = "ar",
        conversation_history: Optional[list] = None,
    ) -> str:
        """
        Fully answers a question using Gemini.
        Called when static confidence is LOW (< 40%).
        """
        try:
            # Build context from conversation history
            context = self._build_context(conversation_history)

            lang_instruction = (
                "أجب باللغة العربية." if language.startswith("ar")
                else "Reply in English."
            )

            prompt = f"{lang_instruction}\n\n{context}السؤال: {user_message}"
            response = self.model.generate_content(prompt)
            return response.text.strip()

        except Exception as e:
            logger.error(f"Gemini answer error: {e}")
            return self._fallback(language)

    def enhance(
        self,
        user_message: str,
        static_response: str,
        language: str = "ar",
    ) -> str:
        """
        Enhances a static response with more personalized detail.
        Called when static confidence is MEDIUM (40-70%).
        """
        try:
            lang_instruction = (
                "أجب باللغة العربية." if language.startswith("ar")
                else "Reply in English."
            )

            prompt = f"""{lang_instruction}

لديك إجابة جاهزة على سؤال المستخدم، قم بتحسينها وجعلها أكثر تفصيلاً وشخصية.

السؤال: {user_message}

الإجابة الجاهزة:
{static_response}

اجعل الإجابة أكثر تفصيلاً وأضف معلومات إضافية مفيدة إن وجدت.
لا تغير المعلومات الطبية الأساسية — فقط أضف تفصيلاً وأسلوباً أفضل.
"""
            response = self.model.generate_content(prompt)
            return response.text.strip()

        except Exception as e:
            logger.error(f"Gemini enhance error: {e}")
            # If Gemini fails, return the original static response
            return static_response

    def _build_context(self, history: Optional[list]) -> str:
        """Builds a context string from conversation history."""
        if not history or len(history) == 0:
            return ""
        # Last 3 exchanges only (to keep prompt short)
        recent = history[-6:]
        lines = []
        for msg in recent:
            role = "المستخدم" if msg["role"] == "user" else "المساعد"
            lines.append(f"{role}: {msg['content'][:100]}")
        return "سياق المحادثة السابقة:\n" + "\n".join(lines) + "\n\n"

    def _fallback(self, language: str) -> str:
        if language.startswith("ar"):
            return (
                "عذراً، حدث خطأ مؤقت في الخدمة. "
                "يمكنك سؤالي عن: أهلية التبرع، خطوات التبرع، "
                "فصائل الدم، أو فوائد التبرع 🩸"
            )
        return (
            "Sorry, a temporary error occurred. "
            "You can ask me about: donation eligibility, donation steps, "
            "blood types, or donation benefits 🩸"
        )

    @classmethod
    def try_init(cls) -> Optional["GeminiService"]:
        """
        Safe initialization — returns None if API key is missing.
        The system works without Gemini (static only mode).
        """
        try:
            return cls()
        except ValueError as e:
            logger.warning(f"⚠️  Gemini not available: {e}")
            logger.warning("⚠️  Running in STATIC-ONLY mode.")
            return None
