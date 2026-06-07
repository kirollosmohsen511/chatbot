"""
Response Generator
==================
Maps each intent to a rich, context-aware response.
Supports both Arabic and English.
"""

import random
from typing import Optional


# ─────────────────────────────────────────────
# Response Templates per Intent
# ─────────────────────────────────────────────

RESPONSES = {

    "greeting": {
        "ar": [
            "أهلاً وسهلاً! 👋 أنا المساعد الذكي لمنصة التبرع بالدم. كيف أقدر أساعدك النهارده؟",
            "مرحباً بك! 🩸 أنا هنا لأجاوب على أي سؤال عن التبرع بالدم. إيه اللي تعايز تعرفه؟",
            "السلام عليكم! 😊 أنا المساعد الذكي لبنك الدم. اسألني عن أي حاجة تخص التبرع بالدم.",
        ],
        "en": [
            "Hello! 👋 I'm the AI assistant for the Blood Donation Platform. How can I help you today?",
            "Hi there! 🩸 I'm here to answer all your questions about blood donation. What would you like to know?",
        ]
    },

    "thanks": {
        "ar": [
            "العفو! 😊 ربنا يجزيك خير على تفكيرك في التبرع — إنت بتساعد في إنقاذ حياة.",
            "على الرحب! 🩸 لو عندك أي سؤال تاني أنا هنا.",
            "يسعدني! 💪 التبرع بالدم بيفرق كتير — شكراً ليك إنك بتفكر فيه.",
        ],
        "en": [
            "You're welcome! 😊 Thank you for thinking about donating — you're potentially saving lives!",
            "My pleasure! 🩸 Feel free to ask anything else.",
        ]
    },

    "donation_process": {
        "ar": [
            """إجراءات التبرع بالدم بسيطة وبتاخد من 30 إلى 45 دقيقة بس 🕐:

**1️⃣ التسجيل**
سجّل بياناتك في المنصة أو في بنك الدم.

**2️⃣ الكشف الطبي**
فحص سريع للضغط والهيموجلوبين والوزن والتأكد من صحتك.

**3️⃣ التبرع الفعلي**
يستغرق من 8 إلى 10 دقائق فقط — الجزء ده بسيط جداً 💉

**4️⃣ فترة الراحة**
15 دقيقة راحة مع عصير أو بسكويت 🍪

**5️⃣ استلام QR Code**
بعد التبرع هتاخد QR Code للتحقق من التبرع وتجميع النقاط 🎯""",
        ],
        "en": [
            """Blood donation is simple and takes 30-45 minutes ⏱️:

**1️⃣ Registration** — Fill in your info at the platform or blood bank.
**2️⃣ Medical check** — Quick check of BP, hemoglobin, and weight.
**3️⃣ Donation** — Only 8-10 minutes! 💉
**4️⃣ Rest** — 15 minutes with juice and cookies 🍪
**5️⃣ QR Code** — Receive your donation QR code and earn points 🎯"""
        ]
    },

    "before_donation": {
        "ar": [
            """نصائح مهمة قبل التبرع بالدم 📋:

✅ **الأكل والشرب**
- اتناول وجبة خفيفة قبل التبرع بساعتين على الأقل
- اشرب كميات وفيرة من المياه (500 مل إضافية يوم التبرع) 💧
- تجنب الوجبات الدسمة والدهنية

✅ **النوم والراحة**
- نام كويس الليلة اللي قبل التبرع (7-8 ساعات)
- تجنب المجهود الشاق يوم التبرع

✅ **الأشياء اللي تجيب معاك**
- بطاقة الهوية الشخصية 🪪
- ملابس مريحة ذات أكمام واسعة

✅ **اللي لازم تتجنبه**
- التدخين قبل التبرع بساعة على الأقل 🚭
- الكحول قبل التبرع بـ 24 ساعة
- الأسبرين قبل التبرع بـ 48 ساعة (للصفائح الدموية)""",
        ],
        "en": [
            """Tips before donating blood 📋:

✅ **Food & Drink** — Eat a light meal 2 hours before. Drink extra water (500ml). Avoid fatty foods.
✅ **Sleep** — Get 7-8 hours of sleep the night before.
✅ **Bring** — Your ID card 🪪, wear loose-sleeved clothing.
✅ **Avoid** — Smoking 1 hour before, alcohol 24 hours before, aspirin 48 hours before."""
        ]
    },

    "after_donation": {
        "ar": [
            """نصائح ما بعد التبرع 🩹:

✅ **فوراً بعد التبرع**
- استرح 15-20 دقيقة في منطقة الراحة
- اشرب عصير أو مياه مع بسكويت 🍪
- لا تقوم بسرعة لتجنب الدوخة

✅ **خلال أول 24 ساعة**
- اشرب 4-6 أكواب مياه إضافية 💧
- تجنب المجهود البدني الشاق
- تجنب حمل أثقال لمدة 24 ساعة
- لو حسيت بدوار اجلس أو استلقي فوراً

✅ **الأكل المفيد**
- لحوم حمراء، سبانخ، عدس (تعويض الحديد) 🥩
- فيتامين C يساعد في امتصاص الحديد 🍊

⏱️ **جسمك بيعوض الدم خلال:**
- السوائل: 24-48 ساعة
- خلايا الدم الحمراء: 4-6 أسابيع
- الحديد: 6-8 أسابيع""",
        ],
        "en": [
            """After donation care 🩹:

✅ **Immediately** — Rest 15-20 minutes, drink juice, don't stand up too fast.
✅ **Next 24 hours** — Drink extra water 💧, avoid heavy exercise, no heavy lifting.
✅ **Eat iron-rich foods** — Red meat, spinach, lentils 🥩
⏱️ **Recovery:** Fluids: 24-48hrs | Red blood cells: 4-6 weeks | Iron: 6-8 weeks"""
        ]
    },

    "frequency": {
        "ar": [
            """كم مرة تقدر تتبرع في السنة؟ 🗓️

**الدم الكامل (Whole Blood):**
- الرجال: كل **90 يوم** (3 أشهر) — حتى **4 مرات** في السنة
- السيدات: كل **120 يوم** (4 أشهر) — حتى **3 مرات** في السنة

**الصفائح الدموية (Platelets):**
- كل **7 أيام** — حتى **24 مرة** في السنة

**البلازما (Plasma):**
- كل **28 يوم** — حتى **13 مرة** في السنة

📱 المنصة بتبعتلك تنبيه أوتوماتيك لما تيجي موعد التبرع التالي!""",
        ],
        "en": [
            """How often can you donate? 🗓️

**Whole Blood:** Men: every 90 days (4x/year) | Women: every 120 days (3x/year)
**Platelets:** Every 7 days (up to 24x/year)
**Plasma:** Every 28 days (up to 13x/year)

📱 The platform sends you automatic reminders when you're eligible again!"""
        ]
    },

    "blood_types": {
        "ar": [
            """فصائل الدم وجدول التوافق 🩸:

**فصائل الدم:** O+، O-، A+، A-، B+، B-، AB+، AB-

**المتبرع العالمي:**
🏆 **O- (السلبية)** — يتبرع لكل الفصائل
يُحتفظ بها للحالات الطارئة دائماً

**المستقبل العالمي:**
🎯 **AB+ (إيجابي)** — يقبل كل الفصائل

**أكثر الفصائل شيوعاً:**
- O+ (38%) | A+ (34%) | B+ (9%)

**جدول التوافق السريع:**
- O+ ← O+، O-
- A+ ← A+، A-، O+، O-
- B+ ← B+، B-، O+، O-
- AB+ ← الكل ✅

💡 فصيلة دمك متاحة في ملفك الشخصي في المنصة""",
        ],
        "en": [
            """Blood Types & Compatibility 🩸:

🏆 **Universal Donor:** O- (donates to everyone)
🎯 **Universal Recipient:** AB+ (receives from everyone)

**Most common:** O+ (38%) | A+ (34%) | B+ (9%)

Quick compatibility:
- O+ receives from: O+, O-
- A+ receives from: A+, A-, O+, O-
- AB+ receives from: everyone ✅"""
        ]
    },

    "health_conditions": {
        "ar": [
            """الحالات الصحية وأثرها على التبرع 🏥:

✅ **يُسمح بالتبرع مع:**
- السكر المضبوط (نسبة السكر طبيعية)
- ضغط الدم المضبوط بالدواء (140/90 أو أقل)
- الربو الخفيف المضبوط
- الغدة الدرقية المعالجة

❌ **لا يُسمح بالتبرع مع:**
- الأمراض المزمنة غير المضبوطة
- التهاب الكبد B أو C
- الإيدز / HIV
- السرطان
- اضطرابات النزيف (هيموفيليا)
- أمراض القلب الخطيرة

⏸️ **تأجيل مؤقت:**
- الأنيميا (حتى يرتفع الهيموجلوبين)
- الالتهابات الحادة (حتى الشفاء التام + 14 يوم)

💡 لو عندك حالة صحية معينة، ابعتلي تفاصيلها وهقدر أخبرك بدقة أكتر.""",
        ],
        "en": [
            """Medical conditions & donation 🏥:

✅ **Allowed with:** Controlled diabetes, controlled BP (≤140/90), mild asthma, treated thyroid.
❌ **Not allowed:** Uncontrolled chronic diseases, Hepatitis B/C, HIV/AIDS, cancer, hemophilia.
⏸️ **Temporary deferral:** Anemia (until Hb improves), active infections (14 days after recovery).

💡 Share your specific condition and I can give you a more precise answer!"""
        ]
    },

    "tattoo_piercing": {
        "ar": [
            """التاتو والثقب وأثرها على التبرع 🎨:

⏳ **فترة الانتظار: 6 أشهر (180 يوم)**

السبب: خطر انتقال التهاب الكبد أو الأمراض عبر الإبر

✅ **تقدر تتبرع بعد 6 أشهر من:**
- أي تاتو (حتى لو من محل محترف)
- ثقب الأذن أو أي جزء من الجسم
- وشم طبي (تاتو للحواجب مثلاً)

📱 **في المنصة:**
سجّل تاريخ التاتو في ملفك الشخصي وهتشوف تلقائياً تاريخ أول تبرع مسموح ليك بيه!""",
        ],
        "en": [
            """Tattoos/Piercings & Blood Donation 🎨:

⏳ **Wait period: 6 months (180 days)** after any tattoo or body piercing.

**Why?** Risk of hepatitis or bloodborne disease transmission via needles.

✅ After 6 months you can donate normally.
📱 Log your tattoo date in your profile and the platform will notify you when you're eligible!"""
        ]
    },

    "pregnancy": {
        "ar": [
            """الحمل والرضاعة والتبرع بالدم 🤱:

❌ **أثناء الحمل:**
التبرع ممنوع تماماً لحماية صحة الأم والجنين.

❌ **أثناء الرضاعة الطبيعية:**
غير مستحسن التبرع لأن الجسم يحتاج كل طاقته لإنتاج الحليب.

✅ **بعد الولادة:**
- بعد الوضع الطبيعي: انتظري **6 أشهر** على الأقل
- بعد القيصرية: انتظري **6 أشهر** على الأقل
- بعد انتهاء الرضاعة: انتظري **3 أشهر** إضافية

🌸 صحتك وصحة طفلك أهم — انتظري الوقت المناسب!""",
        ],
        "en": [
            """Pregnancy & Blood Donation 🤱:

❌ **During pregnancy:** Not allowed — protects mother and baby.
❌ **While breastfeeding:** Not recommended.

✅ **After delivery:** Wait at least 6 months.
✅ **After breastfeeding ends:** Wait 3 additional months.

🌸 Your health comes first — the right time will come!"""
        ]
    },

    "benefits": {
        "ar": [
            """فوائد التبرع بالدم 💪:

**فوائد لصحتك أنت:**
❤️ تحسين صحة القلب وتقليل كثافة الدم
🔥 حرق حوالي 650 سعراً حرارياً لكل تبرع
🔍 فحص صحي مجاني (ضغط، هيموجلوبين، فصيلة دم)
🩸 تحفيز إنتاج خلايا دم حمراء جديدة
🧬 تقليل خطر الإصابة بأمراض القلب والسرطان

**فوائد للمجتمع:**
🏥 إنقاذ حياة حتى 3 أشخاص من كل تبرع واحد
🚨 دعم حالات الطوارئ والعمليات الجراحية
💊 مساعدة مرضى السرطان وأمراض الدم المزمنة

**في منصتنا:**
🎁 تكسب نقاط قابلة للاستبدال بخدمات طبية
🏆 شهادة تقدير إلكترونية لكل تبرع""",
        ],
        "en": [
            """Benefits of donating blood 💪:

**For your health:** ❤️ Better heart health | 🔥 Burns ~650 calories | 🔍 Free health check | 🩸 Stimulates new blood cell production

**For the community:** 🏥 One donation saves up to 3 lives | 🚨 Supports emergency cases | 💊 Helps cancer & chronic disease patients

**On our platform:** 🎁 Earn redeemable points | 🏆 Digital donation certificate"""
        ]
    },

    "safety": {
        "ar": [
            """التبرع بالدم آمن تماماً 😌:

✅ **الإجابة المختصرة: نعم، آمن جداً!**

**لماذا هو آمن؟**
- إبر معقمة ومخصصة للاستخدام مرة واحدة فقط
- المعدات تُستخدم مرة واحدة ثم تُرمى
- الفحص الطبي قبل التبرع يضمن صحتك
- يتم سحب 450 مل فقط (10% من دمك)

**إزاي الجسم بيتعامل مع التبرع؟**
- السوائل بترجع خلال 24-48 ساعة
- خلايا الدم الحمراء بترجع كاملة خلال 4-6 أسابيع
- الألم: حقنة بنج خفيفة بس — مثل وخزة صغيرة جداً

**ممكن أحس بـ:**
- دوخة خفيفة لو وقفت بسرعة (عادي جداً)
- كدمة صغيرة في مكان الإبرة (تختفي في 3-5 أيام)

🩺 لو عندك مخاوف تانية قولي وهفصلها معاك!""",
        ],
        "en": [
            """Blood donation is completely safe 😌:

✅ **Yes, it's very safe!**

**Why safe?** ✓ Sterile single-use needles ✓ Equipment discarded after one use ✓ Pre-screening ensures your health ✓ Only 450ml taken (10% of your blood)

**You might feel:** Slight dizziness if you stand too fast (very normal), small bruise at needle site (fades in 3-5 days).

🩺 The pinch from the needle is minimal — much less than a typical blood test!"""
        ]
    },

    "age_weight": {
        "ar": [
            """شروط السن والوزن للتبرع بالدم ⚖️:

**السن:**
- الحد الأدنى: **18 سنة**
- الحد الأقصى: **65 سنة**
- (في بعض بنوك الدم المتبرعون المنتظمون يكملوا حتى 70)

**الوزن:**
- الحد الأدنى: **50 كيلوجرام**
- لا يوجد حد أقصى للوزن (بشرط الصحة العامة الجيدة)

**لماذا هذه الشروط؟**
- السن: ضمان النضج الجسدي واستقرار الهيموجلوبين
- الوزن: ضمان أن حجم 450 مل لا يمثل نسبة كبيرة من دمك

💡 لو عندك 17 سنة — سجّل في المنصة دلوقتي وهنبعتلك تنبيه أوتوماتيك في عيد ميلادك الـ18! 🎂""",
        ],
        "en": [
            """Age & Weight requirements for donation ⚖️:

**Age:** Minimum 18 | Maximum 65 years
**Weight:** Minimum 50 kg | No maximum (as long as you're healthy)

**Why these limits?**
- Age: ensures physical maturity and stable hemoglobin
- Weight: ensures 450ml doesn't represent too high a % of blood volume

💡 If you're 17 — register now and we'll send you an automatic birthday reminder when you turn 18! 🎂"""
        ]
    },

    "eligibility_check": {
        "ar": [
            """للتحقق من أهليتك للتبرع بدقة، أنا بحتاج بعض المعلومات 🩺:

1️⃣ كم عمرك؟
2️⃣ كم وزنك بالكيلو؟
3️⃣ هل عندك أي أمراض مزمنة؟
4️⃣ هل بتاخد أي أدوية بانتظام؟
5️⃣ امتى كان آخر تبرع؟ (لو تبرعت قبل كده)

💡 **الأسرع:** لو سجّلت بياناتك الطبية في ملفك الشخصي في المنصة، الشات بوت هيقولك على طول هل أنت مؤهل أو لأ!""",
        ],
        "en": [
            """To accurately check your eligibility, I need a few details 🩺:

1️⃣ Your age?
2️⃣ Your weight (kg)?
3️⃣ Any chronic medical conditions?
4️⃣ Any regular medications?
5️⃣ When was your last donation (if any)?

💡 **Faster:** If you fill in your medical profile in the app, I can instantly tell you if you're eligible!"""
        ]
    },

    "unknown": {
        "ar": [
            "مش فاهم سؤالك كويس 😅 ممكن تعيد صياغته؟ أنا متخصص في الإجابة على أسئلة التبرع بالدم.",
            "آسف مش قدرت أفهم سؤالك! جرب تسأل عن: أهلية التبرع، خطوات التبرع، فصائل الدم، أو فوائد التبرع.",
        ],
        "en": [
            "I didn't quite understand that 😅 Could you rephrase? I specialize in blood donation questions.",
            "Sorry, I couldn't understand. Try asking about: eligibility, donation steps, blood types, or donation benefits.",
        ]
    }
}


def get_response(intent: str, language: str = "ar", **context) -> str:
    """
    Returns a response string for the given intent and language.
    Falls back to unknown if intent not found.
    """
    lang = "ar" if language.startswith("ar") else "en"
    responses = RESPONSES.get(intent, RESPONSES["unknown"])
    templates = responses.get(lang, responses.get("ar", ["لم أفهم سؤالك."]))
    return random.choice(templates)
