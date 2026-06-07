"""
Eligibility Engine
==================
Rule-based AI engine that determines blood donation eligibility
based on the user's medical profile sent from the .NET backend.

This is the core "intelligence" for eligibility decisions.
Each rule maps directly to real WHO / Egyptian blood bank guidelines.
"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import date, datetime


# ─────────────────────────────────────────────
# Data Model
# ─────────────────────────────────────────────

@dataclass
class DonorProfile:
    """Represents the user's medical profile from your database."""
    age: Optional[int] = None
    weight_kg: Optional[float] = None
    blood_type: Optional[str] = None
    has_tattoo: Optional[bool] = None
    tattoo_date: Optional[str] = None          # ISO: "2024-06-01"
    last_donation_date: Optional[str] = None   # ISO: "2025-01-15"
    is_pregnant: Optional[bool] = False
    is_breastfeeding: Optional[bool] = False
    medical_conditions: list = field(default_factory=list)
    current_medications: list = field(default_factory=list)
    gender: Optional[str] = None               # "male" / "female"
    hemoglobin: Optional[float] = None         # g/dL
    recent_surgery: Optional[bool] = False
    recent_surgery_months: Optional[int] = None
    had_covid: Optional[bool] = False
    covid_recovery_date: Optional[str] = None


@dataclass
class EligibilityResult:
    """Result of the eligibility check."""
    is_eligible: bool
    reason: str                      # Main reason (Arabic)
    reason_en: str                   # Main reason (English)
    details: list = field(default_factory=list)  # All check details
    wait_days: Optional[int] = None  # Days remaining if temporarily ineligible
    recommendations: list = field(default_factory=list)


# ─────────────────────────────────────────────
# Disqualifying Conditions (permanent)
# ─────────────────────────────────────────────

PERMANENT_DISQUALIFYING_CONDITIONS = [
    "hiv", "aids", "hepatitis_b", "hepatitis_c",
    "cancer", "leukemia", "hemophilia",
    "sickle_cell_anemia", "heart_failure",
    "epilepsy", "schizophrenia",
    "التهاب الكبد ب", "التهاب الكبد ج",
    "سرطان", "إيدز", "هيموفيليا",
]

# Conditions requiring temporary deferral (with wait period in days)
TEMPORARY_CONDITIONS = {
    "cold": 7,
    "flu": 14,
    "infection": 14,
    "malaria": 90,
    "typhoid": 30,
    "brucellosis": 180,
    "زكام": 7,
    "انفلونزا": 14,
    "ملاريا": 90,
}

# Medications requiring deferral
DEFERRING_MEDICATIONS = [
    "aspirin",       # 48 hours wait for platelets
    "warfarin",
    "heparin",
    "isotretinoin",
    "finasteride",
    "أسبرين",
    "وارفارين",
]


# ─────────────────────────────────────────────
# Core Engine
# ─────────────────────────────────────────────

class EligibilityEngine:
    """
    Evaluates blood donation eligibility based on WHO and
    Egyptian Ministry of Health guidelines.
    """

    def evaluate(self, profile: DonorProfile) -> EligibilityResult:
        """
        Runs all eligibility rules and returns a comprehensive result.
        Rules are checked in order of severity.
        """
        details = []

        # ── Rule 1: Age ──────────────────────────────
        if profile.age is not None:
            if profile.age < 18:
                return EligibilityResult(
                    is_eligible=False,
                    reason=f"عمرك {profile.age} سنة — الحد الأدنى للتبرع هو 18 سنة.",
                    reason_en=f"Age {profile.age} is below the minimum of 18 years.",
                    details=details,
                    recommendations=["انتظر حتى تبلغ 18 سنة ثم سجّل في المنصة مرة أخرى ✅"]
                )
            elif profile.age > 65:
                return EligibilityResult(
                    is_eligible=False,
                    reason=f"عمرك {profile.age} سنة — الحد الأقصى للتبرع هو 65 سنة.",
                    reason_en=f"Age {profile.age} exceeds the maximum of 65 years.",
                    details=details,
                    recommendations=["يمكنك دعم منظومة التبرع بالتوعية وتشجيع الآخرين 🙏"]
                )
            else:
                details.append(f"✅ العمر ({profile.age} سنة) مناسب للتبرع.")

        # ── Rule 2: Weight ───────────────────────────
        if profile.weight_kg is not None:
            if profile.weight_kg < 50:
                return EligibilityResult(
                    is_eligible=False,
                    reason=f"وزنك {profile.weight_kg} كجم — الحد الأدنى للوزن هو 50 كجم.",
                    reason_en=f"Weight {profile.weight_kg}kg is below the minimum of 50kg.",
                    details=details,
                    recommendations=["حاول تحسين تغذيتك والوصول لوزن صحي أعلى من 50 كجم 💪"]
                )
            else:
                details.append(f"✅ الوزن ({profile.weight_kg} كجم) مناسب.")

        # ── Rule 3: Pregnancy ────────────────────────
        if profile.is_pregnant:
            return EligibilityResult(
                is_eligible=False,
                reason="لا يجوز التبرع أثناء الحمل لحماية صحة الأم والجنين.",
                reason_en="Blood donation is not permitted during pregnancy.",
                details=details,
                wait_days=None,
                recommendations=["يمكنك التبرع بعد 6 أشهر من الولادة وانتهاء الرضاعة 🌸"]
            )

        # ── Rule 4: Breastfeeding ────────────────────
        if profile.is_breastfeeding:
            return EligibilityResult(
                is_eligible=False,
                reason="لا يُنصح بالتبرع أثناء فترة الرضاعة الطبيعية.",
                reason_en="Donation is not recommended while breastfeeding.",
                details=details,
                recommendations=["انتظري 3 أشهر بعد انتهاء الرضاعة قبل التبرع 🍼"]
            )

        # ── Rule 5: Permanent conditions ─────────────
        if profile.medical_conditions:
            for condition in profile.medical_conditions:
                c = condition.lower().strip()
                for disq in PERMANENT_DISQUALIFYING_CONDITIONS:
                    if disq in c:
                        return EligibilityResult(
                            is_eligible=False,
                            reason=f"حالتك الصحية ({condition}) تمنع التبرع بالدم.",
                            reason_en=f"Medical condition '{condition}' permanently disqualifies donation.",
                            details=details,
                            recommendations=["استشر طبيبك المختص للمزيد من المعلومات 🏥"]
                        )

        # ── Rule 6: Temporary conditions ─────────────
        if profile.medical_conditions:
            for condition in profile.medical_conditions:
                c = condition.lower().strip()
                for temp_cond, wait in TEMPORARY_CONDITIONS.items():
                    if temp_cond in c:
                        return EligibilityResult(
                            is_eligible=False,
                            reason=f"حالتك الصحية الحالية ({condition}) تتطلب تأجيل التبرع.",
                            reason_en=f"Temporary condition '{condition}' requires deferral.",
                            details=details,
                            wait_days=wait,
                            recommendations=[f"انتظر {wait} يوماً من تعافيك الكامل ثم تبرع 💊"]
                        )

        # ── Rule 7: Recent surgery ────────────────────
        if profile.recent_surgery:
            months = profile.recent_surgery_months or 0
            if months < 6:
                remaining = (6 - months) * 30
                return EligibilityResult(
                    is_eligible=False,
                    reason="أجريت عملية جراحية مؤخراً — يجب الانتظار 6 أشهر بعد الجراحة.",
                    reason_en="Recent surgery requires 6-month waiting period.",
                    details=details,
                    wait_days=remaining,
                    recommendations=["تأكد من تعافيك الكامل قبل التبرع 🏥"]
                )

        # ── Rule 8: Tattoo / Piercing ─────────────────
        if profile.has_tattoo and profile.tattoo_date:
            try:
                tattoo_dt = datetime.fromisoformat(profile.tattoo_date).date()
                days_since = (date.today() - tattoo_dt).days
                if days_since < 180:
                    remaining = 180 - days_since
                    return EligibilityResult(
                        is_eligible=False,
                        reason=f"عملت تاتو أو ثقب منذ {days_since} يوم فقط — لازم تنتظر 6 أشهر.",
                        reason_en=f"Tattoo/piercing done {days_since} days ago. Must wait 6 months.",
                        details=details,
                        wait_days=remaining,
                        recommendations=[f"باقي {remaining} يوم وتقدر تتبرع 🎯"]
                    )
                else:
                    details.append("✅ مر أكثر من 6 أشهر على التاتو/الثقب.")
            except ValueError:
                pass

        # ── Rule 9: Last donation date ────────────────
        if profile.last_donation_date:
            try:
                last_dt = datetime.fromisoformat(profile.last_donation_date).date()
                days_since = (date.today() - last_dt).days
                min_gap = 90  # 3 months default
                if profile.gender == "female":
                    min_gap = 120  # 4 months for women

                if days_since < min_gap:
                    remaining = min_gap - days_since
                    return EligibilityResult(
                        is_eligible=False,
                        reason=f"تبرعت منذ {days_since} يوم فقط — الفترة الأدنى بين التبرعات {min_gap} يوم.",
                        reason_en=f"Last donation was {days_since} days ago. Minimum gap is {min_gap} days.",
                        details=details,
                        wait_days=remaining,
                        recommendations=[f"باقي {remaining} يوم وتقدر تتبرع تاني 🩸"]
                    )
                else:
                    details.append(f"✅ مر {days_since} يوم منذ آخر تبرع — مناسب للتبرع.")
            except ValueError:
                pass

        # ── Rule 10: Medications ──────────────────────
        if profile.current_medications:
            for med in profile.current_medications:
                m = med.lower().strip()
                for deferring_med in DEFERRING_MEDICATIONS:
                    if deferring_med in m:
                        return EligibilityResult(
                            is_eligible=False,
                            reason=f"الدواء الذي تأخذه ({med}) يتطلب الانتظار قبل التبرع.",
                            reason_en=f"Medication '{med}' requires deferral before donation.",
                            details=details,
                            recommendations=["استشر طبيبك عن إمكانية التوقف المؤقت عن الدواء قبل التبرع 💊"]
                        )

        # ── Rule 11: Hemoglobin ───────────────────────
        if profile.hemoglobin is not None:
            min_hb = 12.5 if profile.gender == "female" else 13.0
            if profile.hemoglobin < min_hb:
                return EligibilityResult(
                    is_eligible=False,
                    reason=f"مستوى الهيموجلوبين عندك ({profile.hemoglobin} g/dL) منخفض — الحد الأدنى {min_hb} g/dL.",
                    reason_en=f"Hemoglobin {profile.hemoglobin} g/dL is below minimum {min_hb} g/dL.",
                    details=details,
                    recommendations=["اتناول غذاء غني بالحديد مثل السبانخ واللحم الأحمر 🥩"]
                )
            else:
                details.append(f"✅ الهيموجلوبين ({profile.hemoglobin} g/dL) مناسب.")

        # ── All rules passed → ELIGIBLE ───────────────
        return EligibilityResult(
            is_eligible=True,
            reason="أنت مؤهل للتبرع بالدم! 🎉",
            reason_en="You are eligible to donate blood!",
            details=details,
            recommendations=[
                "اشرب 500 مل ماء قبل التبرع بساعة على الأقل 💧",
                "تناول وجبة خفيفة قبل التبرع بساعتين 🍎",
                "احضر بطاقتك الشخصية لتسجيل التبرع 🪪",
                "تجنب التدخين قبل التبرع بساعة 🚭",
            ]
        )


# ── Standalone test ──────────────────────────────────
if __name__ == "__main__":
    engine = EligibilityEngine()

    profile = DonorProfile(
        age=25,
        weight_kg=70,
        gender="male",
        last_donation_date="2025-01-01",
        has_tattoo=False,
        is_pregnant=False,
        medical_conditions=[],
        current_medications=[],
    )

    result = engine.evaluate(profile)
    print(f"Eligible: {result.is_eligible}")
    print(f"Reason: {result.reason}")
    print(f"Details: {result.details}")
    print(f"Recommendations: {result.recommendations}")
