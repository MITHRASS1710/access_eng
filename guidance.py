def get_guidance(category, lang):

    data = {

        # ----------------- HARASSMENT -----------------
        "harassment": {
            "en": {
                "title": "Harassment (Physical & Cyber)",
                "steps": [
                    "Take high-resolution screenshots of chats and profiles",
                    "Do NOT delete conversations, archive them safely",
                    "Record time, location, and witness details",
                    "Report directly to Internal Complaints Committee (ICC) if workplace issue",
                    "Preserve all digital and physical evidence"
                ],
                "laws": [
                    "BNS Section 78: Stalking (Physical or Digital)",
                    "BNS Section 79: Insult to modesty of a woman",
                    "IT Act Section 66E: Violation of privacy"
                ],
                "helpline": [
                    "Kavalan SOS App (Shake to Trigger)",
                    "Cyber Crime Portal: cybercrime.gov.in",
                    "Helpline: 1930"
                ]
            },

            "ta": {
                "title": "துன்புறுத்தல் (உடல் & இணையம்)",
                "steps": [
                    "உரையாடல்கள் மற்றும் சுயவிவரங்களின் ஸ்கிரீன்ஷாட் எடுக்கவும்",
                    "உரையாடலை நீக்காமல் சேமித்து வைக்கவும்",
                    "நேரம், இடம் மற்றும் சாட்சிகளை பதிவு செய்யவும்",
                    "பணியிட பிரச்சினை என்றால் ICC-க்கு நேரடியாக புகார் செய்யவும்",
                    "அனைத்து சான்றுகளையும் பாதுகாக்கவும்"
                ],
                "laws": [
                    "BNS பிரிவு 78: பின்தொடர்தல்",
                    "BNS பிரிவு 79: பெண்களின் கண்ணியத்தை அவமதித்தல்",
                    "IT Act 66E: தனியுரிமை மீறல்"
                ],
                "helpline": [
                    "Kavalan SOS செயலி",
                    "cybercrime.gov.in",
                    "உதவி எண்: 1930"
                ]
            },

            "hi": {
                "title": "उत्पीड़न (शारीरिक और साइबर)",
                "steps": [
                    "चैट और प्रोफाइल के स्क्रीनशॉट लें",
                    "बातचीत डिलीट न करें, सुरक्षित रखें",
                    "समय, स्थान और गवाहों को नोट करें",
                    "कार्यस्थल पर ICC में शिकायत करें",
                    "सभी सबूत सुरक्षित रखें"
                ],
                "laws": [
                    "BNS धारा 78: पीछा करना",
                    "BNS धारा 79: महिला की गरिमा का अपमान",
                    "IT Act 66E: गोपनीयता उल्लंघन"
                ],
                "helpline": [
                    "Kavalan SOS ऐप",
                    "cybercrime.gov.in",
                    "हेल्पलाइन: 1930"
                ]
            }
        },

        # ----------------- INFRASTRUCTURE -----------------
        "infrastructure": {
            "en": {
                "title": "Infrastructure (Safety Audit)",
                "steps": [
                    "Identify dark spots with no lighting",
                    "Document unsafe areas (bushes, broken walls)",
                    "Report missing CCTV in public transport areas",
                    "Submit complaint to municipal authority",
                    "Follow up if unresolved"
                ],
                "laws": [
                    "Article 21: Right to safe infrastructure",
                    "Local bodies must ensure streetlight uptime"
                ],
                "helpline": [
                    "Namma Chennai App",
                    "TANGEDCO: 1912",
                    "CM Helpline: 1100"
                ]
            },

            "ta": {
                "title": "உள்கட்டமைப்பு (பாதுகாப்பு)",
                "steps": [
                    "இருண்ட பகுதிகளை கண்டறியவும்",
                    "பாதுகாப்பற்ற இடங்களை பதிவு செய்யவும்",
                    "CCTV இல்லாத பகுதிகளை புகாரளிக்கவும்",
                    "மாநகராட்சிக்கு தகவல் தெரிவிக்கவும்",
                    "தொடர்ந்து கண்காணிக்கவும்"
                ],
                "laws": [
                    "சட்டப்பிரிவு 21",
                    "தெருவிளக்கு பொறுப்பு"
                ],
                "helpline": [
                    "Namma Chennai App",
                    "1912",
                    "1100"
                ]
            },

            "hi": {
                "title": "बुनियादी ढांचा (सुरक्षा)",
                "steps": [
                    "अंधेरे क्षेत्रों की पहचान करें",
                    "असुरक्षित स्थानों का रिकॉर्ड रखें",
                    "CCTV की कमी की रिपोर्ट करें",
                    "नगर निगम को सूचित करें",
                    "फॉलोअप करें"
                ],
                "laws": [
                    "अनुच्छेद 21",
                    "स्ट्रीटलाइट नियम"
                ],
                "helpline": [
                    "Namma Chennai App",
                    "1912",
                    "1100"
                ]
            }
        },

        # ----------------- DISCRIMINATION -----------------
        "discrimination": {
            "en": {
                "title": "Discrimination (Social & Systemic)",
                "steps": [
                    "Maintain a grievance journal",
                    "Record dates and exact incidents",
                    "File formal complaint via email",
                    "Seek labor department mediation if needed"
                ],
                "laws": [
                    "Article 15: No discrimination",
                    "Equal Remuneration Act",
                    "TN Transgender Policy"
                ],
                "helpline": [
                    "Social Justice: 155811",
                    "Women Commission: 044-28592230"
                ]
            },

            "ta": {
                "title": "பாகுபாடு",
                "steps": [
                    "புகார் நாட்குறிப்பு வைத்திருக்கவும்",
                    "நிகழ்வுகளை பதிவு செய்யவும்",
                    "மின்னஞ்சல் மூலம் புகார் செய்யவும்",
                    "தொழிலாளர் துறையை அணுகவும்"
                ],
                "laws": [
                    "சட்டப்பிரிவு 15",
                    "சம ஊதியம் சட்டம்"
                ],
                "helpline": [
                    "155811",
                    "044-28592230"
                ]
            },

            "hi": {
                "title": "भेदभाव",
                "steps": [
                    "शिकायत जर्नल रखें",
                    "घटनाओं को रिकॉर्ड करें",
                    "ईमेल से शिकायत करें",
                    "श्रम विभाग से मदद लें"
                ],
                "laws": [
                    "अनुच्छेद 15",
                    "समान वेतन अधिनियम"
                ],
                "helpline": [
                    "155811",
                    "044-28592230"
                ]
            }
        },

        # ----------------- SAFETY -----------------
        "safety": {
            "en": {
                "title": "Public Safety",
                "steps": [
                    "Share live location during travel",
                    "Verify vehicle before boarding",
                    "Identify nearby safe zones",
                    "Stay alert in unknown areas"
                ],
                "laws": [
                    "Zero FIR: Can file anywhere",
                    "Right to private defence"
                ],
                "helpline": [
                    "Emergency: 112",
                    "Railway: 1512",
                    "Pink Patrol (Chennai)"
                ]
            },

            "ta": {
                "title": "பாதுகாப்பு",
                "steps": [
                    "Live location பகிரவும்",
                    "வாகனத்தை சரிபார்க்கவும்",
                    "பாதுகாப்பான இடங்களை கண்டறியவும்",
                    "எச்சரிக்கையாக இருங்கள்"
                ],
                "laws": [
                    "Zero FIR",
                    "தற்காப்பு உரிமை"
                ],
                "helpline": [
                    "112",
                    "1512"
                ]
            },

            "hi": {
                "title": "सार्वजनिक सुरक्षा",
                "steps": [
                    "लाइव लोकेशन शेयर करें",
                    "वाहन सत्यापित करें",
                    "सुरक्षित स्थान पहचानें",
                    "सतर्क रहें"
                ],
                "laws": [
                    "Zero FIR",
                    "आत्मरक्षा अधिकार"
                ],
                "helpline": [
                    "112",
                    "1512"
                ]
            }
        }
    }

    return data.get(category, {}).get(lang, {})