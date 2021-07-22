from flask import Markup

# contain information of the Heart Disease

about_page = {
    'title': 'About Heart Disease',
    'brief description': 'Learn about heart disease and its related conditions.',
    'content': [
        {
            'header': 'What is heart disease?',
            'content_1': 'The term “heart disease” refers to several types of heart conditions. \
            The most common type of heart disease in the United States is coronary artery disease (CAD),\
            which affects the blood flow to the heart. Decreased blood flow can cause a heart attack.',
        },

        {
            'header': 'What are the symptoms of heart disease?',
            'content_1': 'Sometimes heart disease may be “silent” and not diagnosed until a person\
            experiences signs or symptoms of a heart attack, heart failure, or an arrhythmia. \
            When these events happen, symptoms may include1',
            'bullet_point' : ['Heart attack: Chest pain or discomfort, upper back or neck pain, indigestion, heartburn, nausea or vomiting, extreme fatigue, upper body discomfort, dizziness, and shortness of breath.',
                        'Arrhythmia: Fluttering feelings in the chest (palpitations).',
                        'Heart failure: Shortness of breath, fatigue, or swelling of the feet, ankles, legs, abdomen, or neck veins.'],
        },

        {
            'header': 'What are the risk factors for heart disease?',
            'content_1': 'High blood pressure, high blood cholesterol, and smoking are \
                key risk factors for heart disease. About half of Americans (47%) have at \
                least one of these three risk factors.2 Several other medical conditions and \
                lifestyle choices can also put people at a higher risk for heart disease, including',
            'bullet_point' : ['Diabetes', 'Overweight and obesity', 'Unhealthy diet', 'Physical inactivity', 'Excessive alcohol use',]
        }
    ],
}

risk_page = {
    'title': 'Risk Factors of Heart Disease',
    'brief description': 'Find out what increases your risk for heart disease.',
    'content': [
        {
            'header': 'Know Your Risk for Heart Disease',
            'content_1': 'Several health conditions, your lifestyle, and your age and family \
            history can increase your risk for heart disease. These are called risk factors. \
            About half of all Americans (47%) have at least 1 of 3 key risk factors for heart \
            disease: high blood pressure, high cholesterol, and smoking.1;',
            'content_2': 'Some risk factors for heart disease cannot be controlled, such as your \
            age or family history. But you can take steps to lower your risk by changing \
            the factors you can control.',
        },
        {
            'header': 'What health conditions increase the risk of heart disease?',
            'content_1': 'High blood pressure. High blood pressure is a major\
            risk factor for heart disease. It is a medical condition that happens when\
            the pressure of the blood in your arteries and other blood vessels is too \
            high. The high pressure, if not controlled, can affect your heart and other\
            major organs of your body, including your kidneys and brain.',

            'content_2': 'High blood pressure is often called a “silent killer” because\
            it usually has no symptoms. The only way to know whether you have high blood \
            pressure is to measure your blood pressure. You can lower your blood pressure \
            with lifestyle changes or with medicine to reduce your risk for heart disease \
            and heart attack. Learn more about blood pressure.',

            'content_3': 'Unhealthy blood cholesterol levels. Cholesterol is a waxy, \
            fat-like substance made by the liver or found in certain foods. Your liver makes\
            enough for your body’s needs, but we often get more cholesterol from the foods we eat.',

            'content_4': 'If we take in more cholesterol than the body can use, the extra \
            cholesterol can build up in the walls of the arteries, including those of the heart. \
            This leads to narrowing of the arteries and can decrease the blood flow to the heart, \
            brain, kidneys, and other parts of the body.',

            'content_5': 'There are two main types of blood cholesterol: LDL (low-density lipoprotein) cholesterol, which is considered to be “bad” cholesterol because it can cause plaque buildup in your arteries, and HDL (high-density lipoprotein) cholesterol, which is considered to be “good” cholesterol because higher levels provide some protection against heart disease.',
            'content_6': 'High blood cholesterol usually has no signs or symptoms. The only way to know whether you have high cholesterol is to get your cholesterol checked. Your health care team can do a simple blood test, called a “lipid profile,” to measure your cholesterol levels. Learn more about getting your cholesterol checked.',
            'content_7': 'Diabetes mellitus. Your body needs glucose (sugar) for energy. Insulin is a hormone made in the pancreas that helps move glucose from the food you eat to your body’s cells for energy. If you have diabetes, your body doesn’t make enough insulin, can’t use its own insulin as well as it should, or both.',
            'content_8': 'Diabetes causes sugar to build up in the blood. The risk of death from heart disease for adults with diabetes is higher than for adults who do not have diabetes.2 Talk with your doctor about ways to prevent or manage diabetes and control other risk factors.',
            'content_9': 'Obesity. Obesity is excess body fat. Obesity is linked to higher “bad” cholesterol and triglyceride levels and to lower “good” cholesterol levels. Obesity can lead to high blood pressure and diabetes as well as heart disease. Talk with your health care team about a plan to reduce your weight to a healthy level. Learn more about healthy weight.',
        },
        {
            'header': 'What behaviors increase the risk of heart disease?',
            'content_1': 'Your lifestyle can increase your risk for heart disease.',
            'bullet_point' : ['Eating a diet high in saturated fats, trans fat, and cholesterol has been linked to heart disease and related conditions, such as atherosclerosis. Also, too much salt (sodium) in the diet can raise blood pressure.',
                    'Not getting enough physical activity can lead to heart disease. It can also increase the chances of having other medical conditions that are risk factors, including obesity, high blood pressure, high cholesterol, and diabetes. Regular physical activity can lower your risk for heart disease.',
                    'Drinking too much alcohol can raise blood pressure levels and the risk for heart disease. It also increases levels of triglycerides, a fatty substance in the blood which can increase the risk for heart disease.',
                    'Tobacco use increases the risk for heart disease and heart attack.'],
        },
        {
            'header': 'How do genetics and family history affect the risk of heart disease?',
            'content_1': 'When members of a family pass traits from one generation to another through genes, that process is called heredity.',
            'content_2': 'Genetic factors likely play some role in high blood pressure, heart disease, and other related conditions. However, it is also likely that people with a family history of heart disease share common environments and other factors that may increase their risk.',
            'content_3': 'The risk for heart disease can increase even more when heredity combines with unhealthy lifestyle choices, such as smoking cigarettes and eating an unhealthy diet.',
        },
        {
            'header': 'Do age and sex affect the risk of heart disease?',
            'content_1': 'Heart disease is the number one killer of both men and women. Heart disease can happen at any age, but the risk goes up as you age.'
        },
        {
            'header': 'Do race and ethnicity affect the risk of heart disease?',
            'content_1': 'Heart disease and stroke can affect anyone, but some groups are more likely to have conditions that increase their risk for cardiovascular disease.',
            'content_1': 'Heart disease is the leading cause of death for people of most racial and ethnic groups in the United States, including African Americans, American Indians and Alaska Natives, and white people. For Asian Americans and Pacific Islanders and Hispanics, heart disease is second only to cancer.3'
        },
    ],
}

prevention_page = {
    'title': 'How to Prevent Heart Disease',
    'brief description': 'Learn what you can do to lower your risk and manage conditions that lead to heart disease.',
    'content': [
        {
            'header': 'Prevent Heart Disease',
            'content_1': 'By living a healthy lifestyle, you can help keep your blood pressure, cholesterol, and blood sugar levels normal and lower your risk for heart disease and heart attack.',
        },
        {
            'header': 'Choose Healthy Habits',
            'content_1': 'You can choose healthy habits to help prevent heart disease.',
            'bullet_point' : ['Choose Healthy Foods and Drinks', 'Keep a Healthy Weight', 'Get Regular Physical Activity', 'Don’t Smoke'],
        },
        {
            'header': 'Take Charge of Your Medical Conditions',
            'content_1': 'If you have high cholesterol, high blood pressure, or diabetes, you can take steps to lower your risk for heart disease.',
            'bullet_point' : ['Check Your Cholesterol', 'Control Your Blood Pressure', 'Manage Your Diabetes', 'Take Your Medicines as Directed', 'Work with Your Health Care Team'],
        }
    ],
}

resources_page = {
    'title': 'Other Resources',
    'brief description': 'Find tools and resources to help your patients.',
    'content': [
        {
            'header': 'Tools and Training',
            'content_1': 'Health professionals can access a variety of tools, resources, and training materials to develop and support programs that focus on preventing heart disease.',
        },
        {
            'header': 'Public Health Programs',
            'bullet_point' : [Markup('<a href="/wisewoman/index.htm">WISEWOMAN</a>'),
                            Markup('<a href="/dhdsp/programs/gis_training/index.htm">Building GIS Capacity for Chronic Disease Surveillance</a>'),
                            Markup('<a href="/dhdsp/programs/stroke_registry.htm">Paul Coverdell National Acute Stroke Program</a>'),
                            Markup('<a href="/dhdsp/programs/sodium_reduction.htm">Sodium Reduction in Communities Program</a>'),
                            Markup('<a href="/diabetes/">Prevention and Management of Diabetes, Heart Disease, and Stroke</a>')],
        },
        {
            'header': 'Tools',
            'content_1': 'Use these tools from Million Hearts® to enhance your heart disease and stroke prevention and treatment efforts.',
            'bullet_point' : [Markup('<a href="https://millionhearts.hhs.gov/tools-protocols/action-guides/tobacco-change-package/index.html" class="tp-link-policy" data-domain-ext="gov">Tobacco Cessation Change Package<span class="sr-only">external icon</span><span class="fi cdc-icon-external x16 fill-external" aria-hidden="true"></span></a>'),
                            Markup('<a href="https://millionhearts.hhs.gov/tools-protocols/action-guides/cardiac-change-package/index.html" class="tp-link-policy" data-domain-ext="gov">Cardiac Rehabilitation Change Package<span class="sr-only">external icon</span><span class="fi cdc-icon-external x16 fill-external" aria-hidden="true"></span></a>'),
                            Markup('<a href="https://millionhearts.hhs.gov/files/HTN_Change_Package.pdf" target="new" class="tp-link-policy" data-domain-ext="gov">Hypertension Control Change Package for Clinicians <span class="sr-only">pdf icon</span><span class="fi cdc-icon-pdf x16 fill-pdf" aria-hidden="true"></span><span class="file-details">[PDF-680K]</span><span class="sr-only">external icon</span><span class="fi cdc-icon-external x16 fill-external" aria-hidden="true"></span></a>'),
                            Markup('<a href="https://millionhearts.hhs.gov/tools-protocols/tools/health-IT.html" class="tp-link-policy" data-domain-ext="gov">Health IT<span class="sr-only">external icon</span><span class="fi cdc-icon-external x16 fill-external" aria-hidden="true"></span></a>'),
                            Markup('<a href="https://nccd.cdc.gov/MillionHearts/Estimator/">Hypertension Prevalence Estimator Tool</a>')],
        },
    ],
}