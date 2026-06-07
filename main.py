"""
Blood Donation AI Chatbot — Hybrid Version 2.0
===============================================
Graduation Project — October 6 University
AI Component by: Kirollos Mohsen Alfons

Architecture:
  Static ML      → fast, guaranteed accurate medical answers
  Gemini AI      → dynamic, handles unexpected questions
  Eligibility    → 11 rule-based medical checks

Run locally:
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
"""

import sys
import os

# Load .env file when running locally
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed — Railway sets env vars automatically

sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import logging

from models.intent_classifier  import IntentClassifier
from models.eligibility_engine import EligibilityEngine, DonorProfile
from models.gemini_service     import GeminiService
from models.hybrid_router      import HybridRouter
from utils.conversation_store  import ConversationStore

# ─────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# FastAPI App
# ─────────────────────────────────────────────
app = FastAPI(
    title="Blood Donation AI Chatbot — Hybrid",
    description=(
        "Hybrid AI chatbot combining Static ML + Google Gemini + Rule-based Eligibility Engine. "
        "Built for the Blood Donation Smart Platform — October 6 University."
    ),
    version="2.0.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "DELETE"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# Load AI Components once at startup
# ─────────────────────────────────────────────
classifier          = IntentClassifier()
eligibility_engine  = EligibilityEngine()
gemini              = GeminiService.try_init()   # None if no API key
router              = HybridRouter(classifier, eligibility_engine, gemini)
conversation_store  = ConversationStore(max_history=10)

logger.info("=" * 50)
logger.info("✅ Blood Donation Chatbot ready.")
logger.info(f"   Mode: {'HYBRID (Static + Gemini)' if gemini else 'STATIC ONLY'}")
logger.info("=" * 50)


# ─────────────────────────────────────────────
# Auth — simple API key for internal service
# ─────────────────────────────────────────────
INTERNAL_API_KEY = os.environ.get("CHATBOT_API_KEY", "blood-donation-secret-key-2025")

def verify_key(x_api_key: str = Header(...)):
    if x_api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return x_api_key


# ─────────────────────────────────────────────
# Pydantic Models
# ─────────────────────────────────────────────

class UserMedicalProfile(BaseModel):
    blood_type:             Optional[str]       = None
    age:                    Optional[int]       = None
    weight_kg:              Optional[float]     = None
    gender:                 Optional[str]       = None   # "male" / "female"
    has_tattoo:             Optional[bool]      = None
    tattoo_date:            Optional[str]       = None   # "2024-06-01"
    last_donation_date:     Optional[str]       = None   # "2025-01-15"
    is_pregnant:            Optional[bool]      = False
    is_breastfeeding:       Optional[bool]      = False
    medical_conditions:     Optional[list[str]] = []
    current_medications:    Optional[list[str]] = []
    hemoglobin:             Optional[float]     = None
    recent_surgery:         Optional[bool]      = False
    recent_surgery_months:  Optional[int]       = None


class ChatRequest(BaseModel):
    user_id:      str
    message:      str
    language:     Optional[str]                = "ar"   # "ar" or "en"
    user_profile: Optional[UserMedicalProfile] = None


class ChatResponse(BaseModel):
    user_id:         str
    reply:           str
    intent:          str
    confidence:      float
    mode:            str                      # static | enhanced | gemini | eligibility
    is_eligible:     Optional[bool]           = None
    wait_days:       Optional[int]            = None
    recommendations: Optional[list[str]]      = []
    gemini_active:   bool                     = False
    timestamp:       str


class ClearHistoryRequest(BaseModel):
    user_id: str


# ─────────────────────────────────────────────
# Main Chat Endpoint
# ─────────────────────────────────────────────

@app.post("/api/chatbot/message", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    _: str = Depends(verify_key)
):
    """
    Main endpoint called by the .NET backend.

    Routing:
    ┌──────────────────────────────────────────────────────────┐
    │  confidence ≥ 70%  →  Static response (instant)          │
    │  confidence 40-70% →  Static + Gemini enhancement        │
    │  confidence < 40%  →  Pure Gemini dynamic answer         │
    │  eligibility intent + profile → Eligibility Engine       │
    └──────────────────────────────────────────────────────────┘
    """

    user_id  = request.user_id.strip()
    message  = request.message.strip()
    language = request.language or "ar"

    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    # Get history for Gemini context
    history = conversation_store.get_history(user_id)

    # Build donor profile if provided
    donor_profile: Optional[DonorProfile] = None
    if request.user_profile:
        p = request.user_profile
        donor_profile = DonorProfile(
            age=p.age,
            weight_kg=p.weight_kg,
            gender=p.gender,
            has_tattoo=p.has_tattoo,
            tattoo_date=p.tattoo_date,
            last_donation_date=p.last_donation_date,
            is_pregnant=p.is_pregnant or False,
            is_breastfeeding=p.is_breastfeeding or False,
            medical_conditions=p.medical_conditions or [],
            current_medications=p.current_medications or [],
            hemoglobin=p.hemoglobin,
            recent_surgery=p.recent_surgery or False,
            recent_surgery_months=p.recent_surgery_months,
        )

    # Route through hybrid system
    result = router.route(
        message=message,
        language=language,
        donor_profile=donor_profile,
        history=history,
    )

    # Save to conversation memory
    conversation_store.add_message(user_id, "user", message)
    conversation_store.add_assistant_with_intent(user_id, result.reply, result.intent)

    logger.info(
        f"User: {user_id} | Mode: {result.mode} | "
        f"Intent: {result.intent} | Conf: {result.confidence:.0%}"
    )

    return ChatResponse(
        user_id=user_id,
        reply=result.reply,
        intent=result.intent,
        confidence=result.confidence,
        mode=result.mode,
        is_eligible=result.is_eligible,
        wait_days=result.wait_days,
        recommendations=result.recommendations,
        gemini_active=gemini is not None,
        timestamp=datetime.utcnow().isoformat() + "Z",
    )


# ─────────────────────────────────────────────
# Supporting Endpoints
# ─────────────────────────────────────────────

@app.get("/api/chatbot/history/{user_id}")
async def get_history(user_id: str, _: str = Depends(verify_key)):
    history = conversation_store.get_history(user_id)
    return {"user_id": user_id, "history": history, "count": len(history)}


@app.delete("/api/chatbot/history")
async def clear_history(
    request: ClearHistoryRequest,
    _: str = Depends(verify_key)
):
    conversation_store.clear(request.user_id)
    return {"message": f"History cleared for user {request.user_id}"}


@app.get("/health")
async def health():
    return {
        "status":    "healthy",
        "version":   "2.0.0",
        "mode":      "hybrid" if gemini else "static_only",
        "gemini":    gemini is not None,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


@app.get("/")
async def root():
    return {
        "service": "Blood Donation AI Chatbot (Hybrid) 🩸",
        "version": "2.0.0",
        "mode":    "hybrid" if gemini else "static_only",
        "docs":    "/docs",
    }
