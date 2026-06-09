"""
Training Data for Blood Donation Chatbot Intent Classifier
Arabic (Fusha + Egyptian Colloquial) + English
"""

TRAINING_DATA = [

    # ─────────────────────────────────────────────
    # Intent: ELIGIBILITY_CHECK
    # ─────────────────────────────────────────────
    # فصحى
    ("هل أقدر أتبرع بالدم؟", "eligibility_check"),
    ("ينفع أتبرع؟", "eligibility_check"),
    ("هل أنا مؤهل للتبرع؟", "eligibility_check"),
    ("عايز أعرف لو أقدر أتبرع", "eligibility_check"),
    ("هل يجوز لي التبرع بالدم؟", "eligibility_check"),
    ("ممكن أتبرع بالدم؟", "eligibility_check"),
    ("أنا عايز أتبرع هل فيه مشكلة؟", "eligibility_check"),
    ("هل عمري مناسب للتبرع؟", "eligibility_check"),
    ("هل وزني كافي للتبرع؟", "eligibility_check"),
    # عامية مصرية
    ("اتبرع ولا ايه؟", "eligibility_check"),
    ("ينفعلي اتبرع بالدم؟", "eligibility_check"),
    ("عايز اتبرع بس مش عارف هعرف ولا لا", "eligibility_check"),
    ("ممكن اعمل تبرع دم؟", "eligibility_check"),
    ("اقدر اتبرع بالدم؟", "eligibility_check"),
    ("فيه مانع اتبرع؟", "eligibility_check"),
    ("ايه الشروط عشان اتبرع؟", "eligibility_check"),
    ("هل مسموحلي اتبرع؟", "eligibility_check"),
    ("عايز اعرف لو اقدر اتبرع ولا لا", "eligibility_check"),
    ("مؤهل للتبرع بالدم؟", "eligibility_check"),
    ("اتبرع بالدم ينفع؟", "eligibility_check"),
    # English
    ("can I donate blood?", "eligibility_check"),
    ("am I eligible to donate?", "eligibility_check"),
    ("can I give blood?", "eligibility_check"),
    ("is it safe for me to donate?", "eligibility_check"),

    # ─────────────────────────────────────────────
    # Intent: DONATION_PROCESS
    # ─────────────────────────────────────────────
    ("إزاي أتبرع بالدم؟", "donation_process"),
    ("خطوات التبرع بالدم إيه؟", "donation_process"),
    ("عايز أعرف عملية التبرع", "donation_process"),
    ("ايه اللي بيحصل وأنا بتبرع؟", "donation_process"),
    ("بيعملوا إيه في التبرع؟", "donation_process"),
    ("كيف تتم عملية التبرع؟", "donation_process"),
    # عامية
    ("ازاي اتبرع بالدم؟", "donation_process"),
    ("التبرع بالدم بيتعمل ازاي؟", "donation_process"),
    ("هيعملوا ايه فيا لما اتبرع؟", "donation_process"),
    ("عملية التبرع بالدم بتاخد قد ايه؟", "donation_process"),
    ("خطوات التبرع ايه هي؟", "donation_process"),
    ("مش فاهم التبرع بيتعمل ازاي", "donation_process"),
    ("التبرع بيأخد وقت قد ايه؟", "donation_process"),
    # English
    ("how do I donate blood?", "donation_process"),
    ("what is the blood donation process?", "donation_process"),
    ("what happens during donation?", "donation_process"),
    ("steps to donate blood", "donation_process"),

    # ─────────────────────────────────────────────
    # Intent: BEFORE_DONATION
    # ─────────────────────────────────────────────
    ("لازم آكل قبل التبرع؟", "before_donation"),
    ("إيه اللي لازم أعمله قبل التبرع؟", "before_donation"),
    ("هل لازم أصحى على صايم؟", "before_donation"),
    ("إيه الأكل المناسب قبل التبرع؟", "before_donation"),
    ("هل أشرب مية قبل التبرع؟", "before_donation"),
    ("نصائح قبل التبرع", "before_donation"),
    # عامية
    ("لازم ياكل ايه قبل ما اتبرع؟", "before_donation"),
    ("هاكل قبل التبرع ولا لا؟", "before_donation"),
    ("لازم اجيب معايا ايه لما اتبرع؟", "before_donation"),
    ("لازم اصحى صايم عشان اتبرع؟", "before_donation"),
    ("هشرب مية قبل التبرع؟", "before_donation"),
    ("ايه اللي هعمله قبل التبرع؟", "before_donation"),
    ("بستعد ازاي للتبرع؟", "before_donation"),
    ("ايه نصايح قبل التبرع؟", "before_donation"),
    # English
    ("what should I eat before donating?", "before_donation"),
    ("how to prepare for blood donation?", "before_donation"),
    ("should I fast before donating?", "before_donation"),
    ("what to do before blood donation?", "before_donation"),

    # ─────────────────────────────────────────────
    # Intent: AFTER_DONATION
    # ─────────────────────────────────────────────
    ("إيه اللي أعمله بعد التبرع؟", "after_donation"),
    ("بعد ما أتبرع أعمل إيه؟", "after_donation"),
    ("هل هحس بتعب بعد التبرع؟", "after_donation"),
    ("ايه الأكل المناسب بعد التبرع؟", "after_donation"),
    ("نصائح بعد التبرع", "after_donation"),
    # عامية
    ("بعد التبرع اعمل ايه؟", "after_donation"),
    ("هحس بايه بعد التبرع؟", "after_donation"),
    ("هتعبان بعد التبرع؟", "after_donation"),
    ("ياكل ايه بعد التبرع؟", "after_donation"),
    ("بعد التبرع بالدم اعمل ايه؟", "after_donation"),
    ("هيجيلي دوخة بعد التبرع؟", "after_donation"),
    ("لازم ارتاح بعد التبرع قد ايه؟", "after_donation"),
    ("ايه نصايح بعد التبرع؟", "after_donation"),
    # English
    ("what to do after donating blood?", "after_donation"),
    ("how to recover after blood donation?", "after_donation"),
    ("will I feel weak after donating?", "after_donation"),
    ("what should I eat after donation?", "after_donation"),

    # ─────────────────────────────────────────────
    # Intent: FREQUENCY
    # ─────────────────────────────────────────────
    ("كل قد إيه أقدر أتبرع؟", "frequency"),
    ("متى أقدر أتبرع تاني؟", "frequency"),
    ("كم مرة في السنة ممكن أتبرع؟", "frequency"),
    ("الفترة بين التبرعات كام يوم؟", "frequency"),
    ("كم يوم بين كل تبرع وتاني؟", "frequency"),
    # عامية
    ("اتبرع تاني امتى؟", "frequency"),
    ("بعد كام يوم اقدر اتبرع تاني؟", "frequency"),
    ("المفروض انتظر قد ايه بين التبرعات؟", "frequency"),
    ("كام مرة في السنة اتبرع؟", "frequency"),
    ("بين التبرع والتاني كام يوم؟", "frequency"),
    ("اقدر اتبرع كل شهر؟", "frequency"),
    ("امتى يجيلي دور اتبرع تاني؟", "frequency"),
    # English
    ("how often can I donate blood?", "frequency"),
    ("when can I donate again?", "frequency"),
    ("how many times per year can I donate?", "frequency"),
    ("what is the waiting period between donations?", "frequency"),

    # ─────────────────────────────────────────────
    # Intent: BLOOD_TYPES
    # ─────────────────────────────────────────────
    ("فصائل الدم إيه؟", "blood_types"),
    ("إيه الفرق بين فصائل الدم؟", "blood_types"),
    ("مين يقدر ياخد من مين؟", "blood_types"),
    ("فصيلة O+ تتبرع لمين؟", "blood_types"),
    # عامية
    ("فصيلة دمي ايه معناها؟", "blood_types"),
    ("فصايل الدم ايه هي؟", "blood_types"),
    ("فصيلتي O مينفعش تاخد منين؟", "blood_types"),
    ("مين المتبرع العالمي؟", "blood_types"),
    ("فصيلة AB تاخد من مين؟", "blood_types"),
    ("فصيلة دمي نادرة؟", "blood_types"),
    ("ايه اكتر فصيلة دم مطلوبة؟", "blood_types"),
    # English
    ("what are blood types?", "blood_types"),
    ("who can donate to whom?", "blood_types"),
    ("what is a universal donor?", "blood_types"),
    ("blood type compatibility", "blood_types"),
    ("O negative universal donor", "blood_types"),
    ("AB blood type", "blood_types"),

    # ─────────────────────────────────────────────
    # Intent: HEALTH_CONDITIONS
    # ─────────────────────────────────────────────
    ("هل أقدر أتبرع وأنا عندي سكر؟", "health_conditions"),
    ("مريض ضغط ينفع يتبرع؟", "health_conditions"),
    ("هل أتبرع وأنا بآخد دواء؟", "health_conditions"),
    ("عندي أنيميا هل أتبرع؟", "health_conditions"),
    ("مريض قلب يتبرع؟", "health_conditions"),
    ("هل السرطان يمنع التبرع؟", "health_conditions"),
    # عامية
    ("عندي سكر اتبرع ولا لا؟", "health_conditions"),
    ("عندي ضغط اتبرع ينفع؟", "health_conditions"),
    ("باخد دوا اتبرع ينفع؟", "health_conditions"),
    ("عندي انيميا اتبرع؟", "health_conditions"),
    ("مريض قلب اتبرع بالدم؟", "health_conditions"),
    ("عندي ربو اتبرع؟", "health_conditions"),
    ("عندي مشكلة في الكبد اتبرع؟", "health_conditions"),
    ("باخد حبوب منع حمل اتبرع؟", "health_conditions"),
    ("عندي مشكلة في الغدة اتبرع؟", "health_conditions"),
    ("عندي التهاب اتبرع؟", "health_conditions"),
    # English
    ("can diabetics donate blood?", "health_conditions"),
    ("can I donate if I take medication?", "health_conditions"),
    ("does high blood pressure prevent donation?", "health_conditions"),
    ("can anemic people donate?", "health_conditions"),
    ("I have asthma can I donate?", "health_conditions"),

    # ─────────────────────────────────────────────
    # Intent: TATTOO_PIERCING
    # ─────────────────────────────────────────────
    ("عندي تاتو هل أقدر أتبرع؟", "tattoo_piercing"),
    ("التاتو بيمنع التبرع بالدم؟", "tattoo_piercing"),
    ("عملت ثقب في أذني ينفع أتبرع؟", "tattoo_piercing"),
    ("كام شهر بعد التاتو أقدر أتبرع؟", "tattoo_piercing"),
    # عامية
    ("عندي تاتو اتبرع ينفع؟", "tattoo_piercing"),
    ("عملت تاتو من شهر اتبرع ينفع؟", "tattoo_piercing"),
    ("عملت ثقب اتبرع ينفع؟", "tattoo_piercing"),
    ("بعد التاتو بكام اتبرع؟", "tattoo_piercing"),
    ("التاتو بيأثر على التبرع؟", "tattoo_piercing"),
    ("عملت رسم على جسمي اتبرع؟", "tattoo_piercing"),
    # English
    ("can I donate if I have a tattoo?", "tattoo_piercing"),
    ("tattoo and blood donation", "tattoo_piercing"),
    ("piercing and blood donation", "tattoo_piercing"),
    ("how long after tattoo can I donate?", "tattoo_piercing"),

    # ─────────────────────────────────────────────
    # Intent: PREGNANCY
    # ─────────────────────────────────────────────
    ("هل الحامل تتبرع؟", "pregnancy"),
    ("أنا حامل ينفع أتبرع؟", "pregnancy"),
    ("بعد الولادة بقد إيه أتبرع؟", "pregnancy"),
    ("المرضعة تتبرع بالدم؟", "pregnancy"),
    # عامية
    ("انا حامل اتبرع؟", "pregnancy"),
    ("حامل واتبرع ينفع؟", "pregnancy"),
    ("بعد الولادة باتبرع امتى؟", "pregnancy"),
    ("بترضع اتبرع بالدم؟", "pregnancy"),
    ("في فترة الرضاعة اتبرع؟", "pregnancy"),
    ("ولدت من شهر اتبرع؟", "pregnancy"),
    # English
    ("can pregnant women donate blood?", "pregnancy"),
    ("can I donate while breastfeeding?", "pregnancy"),
    ("how long after pregnancy can I donate?", "pregnancy"),

    # ─────────────────────────────────────────────
    # Intent: BENEFITS
    # ─────────────────────────────────────────────
    ("إيه فوائد التبرع بالدم؟", "benefits"),
    ("التبرع بالدم بيفيد إيه؟", "benefits"),
    ("هل التبرع بالدم مفيد للمتبرع؟", "benefits"),
    ("ليه أتبرع بالدم؟", "benefits"),
    # عامية
    ("التبرع بالدم بيفيد ايه؟", "benefits"),
    ("ايه الفايدة من التبرع بالدم؟", "benefits"),
    ("ليه اتبرع بالدم اصلا؟", "benefits"),
    ("التبرع بالدم كويس للصحة؟", "benefits"),
    ("هيجيلي ايه من التبرع بالدم؟", "benefits"),
    ("فايدة التبرع بالدم ايه؟", "benefits"),
    # English
    ("what are the benefits of donating blood?", "benefits"),
    ("is blood donation good for health?", "benefits"),
    ("does donating blood have health benefits?", "benefits"),
    ("why should I donate blood?", "benefits"),

    # ─────────────────────────────────────────────
    # Intent: SAFETY
    # ─────────────────────────────────────────────
    ("هل التبرع بالدم آمن؟", "safety"),
    ("خايف من التبرع بالدم", "safety"),
    ("هل فيه مخاطر من التبرع؟", "safety"),
    ("هل الإبرة بتوجع؟", "safety"),
    ("هل ممكن أتعدى بمرض من التبرع؟", "safety"),
    # عامية
    ("التبرع بالدم آمن؟", "safety"),
    ("خايف اتبرع بالدم", "safety"),
    ("الابره بتوجع اوي؟", "safety"),
    ("التبرع مؤلم؟", "safety"),
    ("هيتعدالي حاجة لو اتبرعت؟", "safety"),
    ("التبرع بيأذي؟", "safety"),
    ("في خطر من التبرع بالدم؟", "safety"),
    ("التبرع مضر ولا لا؟", "safety"),
    # English
    ("is blood donation safe?", "safety"),
    ("are there risks in donating blood?", "safety"),
    ("I am scared to donate blood", "safety"),
    ("does donation hurt?", "safety"),

    # ─────────────────────────────────────────────
    # Intent: AGE_WEIGHT
    # ─────────────────────────────────────────────
    ("الحد الأدنى للسن للتبرع كام؟", "age_weight"),
    ("أنا عندي 17 سنة أقدر أتبرع؟", "age_weight"),
    ("كبار السن يتبرعوا؟", "age_weight"),
    ("الوزن المطلوب للتبرع كام؟", "age_weight"),
    # عامية
    ("عندي 16 سنة اتبرع ينفع؟", "age_weight"),
    ("عندي 17 سنة اتبرع بالدم؟", "age_weight"),
    ("لازم يكون عندي كام سنة عشان اتبرع؟", "age_weight"),
    ("وزني 45 كيلو اتبرع؟", "age_weight"),
    ("لازم يكون وزني كام عشان اتبرع؟", "age_weight"),
    ("سني كبير اتبرع بالدم؟", "age_weight"),
    ("عندي 60 سنة اتبرع؟", "age_weight"),
    ("الوزن الاقل للتبرع كام؟", "age_weight"),
    # English
    ("what is the minimum age to donate?", "age_weight"),
    ("can teenagers donate blood?", "age_weight"),
    ("minimum weight to donate blood?", "age_weight"),
    ("I am 16 can I donate?", "age_weight"),
    ("الحد الأقصى للسن للتبرع", "age_weight"),

    # ─────────────────────────────────────────────
    # Intent: GREETING
    # ─────────────────────────────────────────────
    ("أهلاً", "greeting"),
    ("مرحباً", "greeting"),
    ("السلام عليكم", "greeting"),
    ("هاي", "greeting"),
    ("صباح الخير", "greeting"),
    ("مساء الخير", "greeting"),
    # عامية
    ("ازيك", "greeting"),
    ("ازيك يا شاطر", "greeting"),
    ("هلو", "greeting"),
    ("هاي عامل ايه", "greeting"),
    ("ايه الاخبار", "greeting"),
    ("يسلمو", "greeting"),
    ("هاي كيفك", "greeting"),
    # English
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("good morning", "greeting"),

    # ─────────────────────────────────────────────
    # Intent: THANKS
    # ─────────────────────────────────────────────
    ("شكراً", "thanks"),
    ("شكرا جزيلاً", "thanks"),
    ("متشكر", "thanks"),
    ("جزاك الله خيراً", "thanks"),
    # عامية
    ("تسلم", "thanks"),
    ("مشكور", "thanks"),
    ("تسلم ايدك", "thanks"),
    ("ربنا يخليك", "thanks"),
    ("شكرا جدا", "thanks"),
    ("الف شكر", "thanks"),
    ("شكرا يسطا", "thanks"),
    # English
    ("thanks", "thanks"),
    ("thank you", "thanks"),
    ("thanks a lot", "thanks"),

    # ─────────────────────────────────────────────
    # Intent: UNKNOWN
    # ─────────────────────────────────────────────
    ("كلام عشوائي", "unknown"),
    ("لا أعرف", "unknown"),
    ("random text here 123", "unknown"),
    ("مش فاهم", "unknown"),
    ("اللي انت شايفه", "unknown"),
]
