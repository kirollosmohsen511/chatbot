"""
Intent Classifier
=================
Uses TF-IDF vectorization + Logistic Regression to classify
the user's message into a specific intent category.

Why this approach?
- Works offline, no external API needed
- Fast inference (< 10ms per message)
- Easy to retrain with new data
- Handles both Arabic and English
"""

import pickle
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from data.training_data import TRAINING_DATA


MODEL_PATH = os.path.join(os.path.dirname(__file__), "intent_model.pkl")


def train_model() -> Pipeline:
    """
    Trains the intent classification model.
    Called once at startup if no saved model exists.
    """
    print("🔧 Training intent classifier...")

    texts  = [item[0] for item in TRAINING_DATA]
    labels = [item[1] for item in TRAINING_DATA]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            analyzer="char_wb",   # character n-grams — great for Arabic
            ngram_range=(2, 4),
            max_features=5000,
            sublinear_tf=True,
        )),
        ("clf", LogisticRegression(
            max_iter=1000,
            C=5.0,
            solver="lbfgs",
        )),
    ])

    pipeline.fit(texts, labels)

    # Quick cross-validation check
    scores = cross_val_score(pipeline, texts, labels, cv=3, scoring="accuracy")
    print(f"✅ Model trained — CV Accuracy: {scores.mean():.2%} ± {scores.std():.2%}")

    # Save model to disk
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(pipeline, f)
    print(f"💾 Model saved to {MODEL_PATH}")

    return pipeline


def load_model() -> Pipeline:
    """Loads existing model or trains a new one."""
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    return train_model()


class IntentClassifier:
    """
    Main classifier class used by the chatbot.

    Usage:
        clf = IntentClassifier()
        result = clf.classify("هل أقدر أتبرع؟")
        # result = {"intent": "eligibility_check", "confidence": 0.94}
    """

    def __init__(self):
        self.model = load_model()

    def classify(self, text: str) -> dict:
        """
        Classifies user input into an intent with a confidence score.

        Returns:
            {
                "intent": str,       # e.g. "eligibility_check"
                "confidence": float, # 0.0 to 1.0
                "all_scores": dict   # scores for all intents
            }
        """
        text = text.strip()
        if not text:
            return {"intent": "unknown", "confidence": 0.0, "all_scores": {}}

        proba = self.model.predict_proba([text])[0]
        classes = self.model.classes_
        scores = dict(zip(classes, proba))

        best_intent = max(scores, key=scores.get)
        confidence = scores[best_intent]

        # If confidence is too low, return unknown
        if confidence < 0.30:
            best_intent = "unknown"

        return {
            "intent": best_intent,
            "confidence": round(float(confidence), 3),
            "all_scores": {k: round(float(v), 3) for k, v in scores.items()}
        }

    def retrain(self):
        """Retrains the model (call this after adding new training data)."""
        if os.path.exists(MODEL_PATH):
            os.remove(MODEL_PATH)
        self.model = train_model()


# ── Allow running this file directly to train & test the model ──
if __name__ == "__main__":
    clf = IntentClassifier()

    test_cases = [
        "هل أقدر أتبرع وأنا مريض سكر؟",
        "can I donate blood after getting a tattoo?",
        "إيه فوائد التبرع بالدم؟",
        "كل قد إيه أتبرع؟",
        "أنا عندي 16 سنة ينفع أتبرع؟",
        "هل الحامل تتبرع بالدم؟",
        "مرحباً",
        "شكراً جزيلاً",
    ]

    print("\n── Test Results ──")
    for text in test_cases:
        result = clf.classify(text)
        print(f"  '{text}'")
        print(f"    → Intent: {result['intent']} (confidence: {result['confidence']})\n")
