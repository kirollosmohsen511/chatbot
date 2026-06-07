"""
Training Data for Blood Donation Chatbot Intent Classifier
Arabic + English bilingual support
"""

TRAINING_DATA = [

    # ─────────────────────────────────────────────
    # Intent: ELIGIBILITY_CHECK — هل أقدر أتبرع؟
    # ─────────────────────────────────────────────
    ("هل أقدر أتبرع بالدم؟", "eligibility_check"),
    ("ينفع أتبرع؟", "eligibility_check"),
    ("هل أنا مؤهل للتبرع؟", "eligibility_check"),
    ("عايز أعرف لو أقدر أتبرع", "eligibility_check"),
    ("هل يجوز لي التبرع بالدم؟", "eligibility_check"),
    ("ممكن أتبرع بالدم؟", "eligibility_check"),
    ("can I donate blood?", "eligibility_check"),
    ("am I eligible to donate?", "eligibility_check"),
    ("can I give blood?", "eligibility_check"),
    ("is it safe for me to donate?", "eligibility_check"),
    ("أنا عايز أتبرع هل فيه مشكلة؟", "eligibility_check"),
    ("هل عمري مناسب للتبرع؟", "eligibility_check"),
    ("هل وزني كافي للتبرع؟", "eligibility_check"),

    # ─────────────────────────────────────────────
    # Intent: DONATION_PROCESS — إزاي أتبرع؟
    # ─────────────────────────────────────────────
    ("إزاي أتبرع بالدم؟", "donation_process"),
    ("خطوات التبرع بالدم إيه؟", "donation_process"),
    ("عايز أعرف عملية التبرع", "donation_process"),
    ("ايه اللي بيحصل وأنا بتبرع؟", "donation_process"),
    ("بيعملوا إيه في التبرع؟", "donation_process"),
    ("how do I donate blood?", "donation_process"),
    ("what is the blood donation process?", "donation_process"),
    ("what happens during donation?", "donation_process"),
    ("steps to donate blood", "donation_process"),
    ("كيف تتم عملية التبرع؟", "donation_process"),
    ("ما هي خطوات التبرع بالدم؟", "donation_process"),

    # ─────────────────────────────────────────────
    # Intent: BEFORE_DONATION — قبل التبرع
    # ─────────────────────────────────────────────
    ("لازم آكل قبل التبرع؟", "before_donation"),
    ("إيه اللي لازم أعمله قبل التبرع؟", "before_donation"),
    ("هل لازم أصحى على صايم؟", "before_donation"),
    ("إيه الأكل المناسب قبل التبرع؟", "before_donation"),
    ("كيف أستعد للتبرع بالدم؟", "before_donation"),
    ("ما الذي يجب فعله قبل التبرع؟", "before_donation"),
    ("what should I eat before donating?", "before_donation"),
    ("how to prepare for blood donation?", "before_donation"),
    ("should I fast before donating?", "before_donation"),
    ("what to do before blood donation?", "before_donation"),
    ("هل أشرب مية قبل التبرع؟", "before_donation"),
    ("نصائح قبل التبرع", "before_donation"),

    # ─────────────────────────────────────────────
    # Intent: AFTER_DONATION — بعد التبرع
    # ─────────────────────────────────────────────
    ("إيه اللي أعمله بعد التبرع؟", "after_donation"),
    ("بعد ما أتبرع أعمل إيه؟", "after_donation"),
    ("كيف أتعافى بعد التبرع؟", "after_donation"),
    ("هل هحس بتعب بعد التبرع؟", "after_donation"),
    ("ايه الأكل المناسب بعد التبرع؟", "after_donation"),
    ("what to do after donating blood?", "after_donation"),
    ("how to recover after blood donation?", "after_donation"),
    ("will I feel weak after donating?", "after_donation"),
    ("what should I eat after donation?", "after_donation"),
    ("متى يرجع الدم بعد التبرع؟", "after_donation"),
    ("نصائح بعد التبرع", "after_donation"),

    # ─────────────────────────────────────────────
    # Intent: FREQUENCY — كل قد إيه أتبرع؟
    # ─────────────────────────────────────────────
    ("كل قد إيه أقدر أتبرع؟", "frequency"),
    ("متى أقدر أتبرع تاني؟", "frequency"),
    ("كم مرة في السنة ممكن أتبرع؟", "frequency"),
    ("الفترة بين التبرعات كام يوم؟", "frequency"),
    ("how often can I donate blood?", "frequency"),
    ("when can I donate again?", "frequency"),
    ("how many times per year can I donate?", "frequency"),
    ("what is the waiting period between donations?", "frequency"),
    ("كم يوم بين كل تبرع وتاني؟", "frequency"),
    ("المدة المسموح بيها بين التبرعات", "frequency"),

    # ─────────────────────────────────────────────
    # Intent: BLOOD_TYPES — فصائل الدم
    # ─────────────────────────────────────────────
    ("فصائل الدم إيه؟", "blood_types"),
    ("إيه الفرق بين فصائل الدم؟", "blood_types"),
    ("مين يقدر ياخد من مين؟", "blood_types"),
    ("ايه فصيلة الدم الأكثر طلباً؟", "blood_types"),
    ("what are blood types?", "blood_types"),
    ("who can donate to whom?", "blood_types"),
    ("what is a universal donor?", "blood_types"),
    ("blood type compatibility", "blood_types"),
    ("فصيلة O+ تتبرع لمين؟", "blood_types"),
    ("O negative universal donor", "blood_types"),
    ("AB blood type", "blood_types"),

    # ─────────────────────────────────────────────
    # Intent: HEALTH_CONDITIONS — حالات صحية
    # ─────────────────────────────────────────────
    ("هل أقدر أتبرع وأنا عندي سكر؟", "health_conditions"),
    ("مريض ضغط ينفع يتبرع؟", "health_conditions"),
    ("هل أتبرع وأنا بآخد دواء؟", "health_conditions"),
    ("عندي أنيميا هل أتبرع؟", "health_conditions"),
    ("هل الأمراض المزمنة تمنع التبرع؟", "health_conditions"),
    ("can diabetics donate blood?", "health_conditions"),
    ("can I donate if I take medication?", "health_conditions"),
    ("does high blood pressure prevent donation?", "health_conditions"),
    ("can anemic people donate?", "health_conditions"),
    ("I have asthma can I donate?", "health_conditions"),
    ("مريض قلب يتبرع؟", "health_conditions"),
    ("هل السرطان يمنع التبرع؟", "health_conditions"),

    # ─────────────────────────────────────────────
    # Intent: TATTOO_PIERCING — تاتو وثقب
    # ─────────────────────────────────────────────
    ("عندي تاتو هل أقدر أتبرع؟", "tattoo_piercing"),
    ("التاتو بيمنع التبرع بالدم؟", "tattoo_piercing"),
    ("عملت ثقب في أذني ينفع أتبرع؟", "tattoo_piercing"),
    ("can I donate if I have a tattoo?", "tattoo_piercing"),
    ("tattoo and blood donation", "tattoo_piercing"),
    ("piercing and blood donation", "tattoo_piercing"),
    ("how long after tattoo can I donate?", "tattoo_piercing"),
    ("كام شهر بعد التاتو أقدر أتبرع؟", "tattoo_piercing"),

    # ─────────────────────────────────────────────
    # Intent: PREGNANCY — الحمل والرضاعة
    # ─────────────────────────────────────────────
    ("هل الحامل تتبرع؟", "pregnancy"),
    ("أنا حامل ينفع أتبرع؟", "pregnancy"),
    ("بعد الولادة بقد إيه أتبرع؟", "pregnancy"),
    ("المرضعة تتبرع بالدم؟", "pregnancy"),
    ("can pregnant women donate blood?", "pregnancy"),
    ("can I donate while breastfeeding?", "pregnancy"),
    ("how long after pregnancy can I donate?", "pregnancy"),

    # ─────────────────────────────────────────────
    # Intent: BENEFITS — فوائد التبرع
    # ─────────────────────────────────────────────
    ("إيه فوائد التبرع بالدم؟", "benefits"),
    ("التبرع بالدم بيفيد إيه؟", "benefits"),
    ("هل التبرع بالدم مفيد للمتبرع؟", "benefits"),
    ("فوائد التبرع على الصحة", "benefits"),
    ("what are the benefits of donating blood?", "benefits"),
    ("is blood donation good for health?", "benefits"),
    ("does donating blood have health benefits?", "benefits"),
    ("why should I donate blood?", "benefits"),
    ("ليه أتبرع بالدم؟", "benefits"),

    # ─────────────────────────────────────────────
    # Intent: SAFETY — أمان التبرع
    # ─────────────────────────────────────────────
    ("هل التبرع بالدم آمن؟", "safety"),
    ("خايف من التبرع بالدم", "safety"),
    ("هل فيه مخاطر من التبرع؟", "safety"),
    ("التبرع بالدم بيأثر على صحتي؟", "safety"),
    ("is blood donation safe?", "safety"),
    ("are there risks in donating blood?", "safety"),
    ("I am scared to donate blood", "safety"),
    ("does donation hurt?", "safety"),
    ("هل الإبرة بتوجع؟", "safety"),
    ("هل ممكن أتعدى بمرض من التبرع؟", "safety"),

    # ─────────────────────────────────────────────
    # Intent: AGE_WEIGHT — السن والوزن
    # ─────────────────────────────────────────────
    ("الحد الأدنى للسن للتبرع كام؟", "age_weight"),
    ("أنا عندي 17 سنة أقدر أتبرع؟", "age_weight"),
    ("كبار السن يتبرعوا؟", "age_weight"),
    ("الوزن المطلوب للتبرع كام؟", "age_weight"),
    ("what is the minimum age to donate?", "age_weight"),
    ("can teenagers donate blood?", "age_weight"),
    ("minimum weight to donate blood?", "age_weight"),
    ("I am 16 can I donate?", "age_weight"),
    ("الحد الأقصى للسن للتبرع", "age_weight"),

    # ─────────────────────────────────────────────
    # Intent: GREETING — تحية
    # ─────────────────────────────────────────────
    ("أهلاً", "greeting"),
    ("مرحباً", "greeting"),
    ("السلام عليكم", "greeting"),
    ("هاي", "greeting"),
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("good morning", "greeting"),
    ("صباح الخير", "greeting"),
    ("مساء الخير", "greeting"),

    # ─────────────────────────────────────────────
    # Intent: THANKS — شكر
    # ─────────────────────────────────────────────
    ("شكراً", "thanks"),
    ("شكرا جزيلاً", "thanks"),
    ("متشكر", "thanks"),
    ("thanks", "thanks"),
    ("thank you", "thanks"),
    ("thanks a lot", "thanks"),
    ("جزاك الله خيراً", "thanks"),

    # ─────────────────────────────────────────────
    # Intent: UNKNOWN — مش واضح
    # ─────────────────────────────────────────────
    ("كلام عشوائي", "unknown"),
    ("لا أعرف", "unknown"),
    ("random text here 123", "unknown"),
]
