# user.py
from dash import html, dcc, Input, Output, State
import dash
import dash_bootstrap_components as dbc
import database

# ---------------- TRANSLATIONS ----------------
translations = {
    "en": {
        "title": "User Complaint Portal",
        "category": "Select Category",
        "issue": "Select Issue",
        "desc": "Detailed Description",
        "anonymous": "Submit Anonymously",
        "name": "Name",
        "phone": "Contact Number",
        "submit": "Submit",
        "success": "Complaint submitted successfully!",
        "error": "Please fill all required fields"
    },
    "ta": {
        "title": "புகார் பதிவு மையம்",
        "category": "வகையை தேர்ந்தெடுக்கவும்",
        "issue": "பிரச்சினையை தேர்ந்தெடுக்கவும்",
        "desc": "விவரம்",
        "anonymous": "அடையாளம் தெரியாமல்",
        "name": "பெயர்",
        "phone": "தொலைபேசி எண்",
        "submit": "சமர்ப்பிக்கவும்",
        "success": "புகார் வெற்றிகரமாக சமர்ப்பிக்கப்பட்டது!",
        "error": "தேவையான தகவல்களை நிரப்பவும்"
    },
    "hi": {
        "title": "शिकायत पोर्टल",
        "category": "श्रेणी चुनें",
        "issue": "समस्या चुनें",
        "desc": "विवरण",
        "anonymous": "गुमनाम",
        "name": "नाम",
        "phone": "फोन नंबर",
        "submit": "जमा करें",
        "success": "शिकायत सफलतापूर्वक जमा हुई!",
        "error": "सभी आवश्यक जानकारी भरें"
    }
}

# ---------------- USER LAYOUT ----------------
layout = dbc.Container([

    html.H2(id="user-title", className="text-center mb-4 fw-bold"),

    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody([

                    # 🔷 CATEGORY
                    dbc.Label(id="label-category", className="mb-1 fw-semibold"),
                    dcc.Dropdown(id="main-category", className="mb-3"),

                    # 🔷 SUB CATEGORY
                    dbc.Label(id="label-issue", className="mb-1 fw-semibold"),
                    dcc.Dropdown(id="sub-category", className="mb-3"),

                    # 🔷 DESCRIPTION
                    dbc.Label(id="label-desc", className="mb-1 fw-semibold"),
                    dbc.Textarea(
                        id="description",
                        placeholder="Describe your issue in detail...",
                        style={
                            "width": "100%",
                            "height": "120px",
                            "borderRadius": "10px"
                        },
                        className="mb-2"
                    ),

                    # 🎤 VOICE BUTTON (PREMIUM)
                    dbc.Button(
                        "🎤 Speak",
                        id="mic-btn",
                        color="danger",
                        outline=True,
                        className="mb-2"
                    ),

                    html.Div(
                        id="voice-status",
                        className="mb-3",
                        style={"fontSize": "14px"}
                    ),

                    # 🔷 ANONYMOUS
                    dbc.Checklist(
                        options=[{"label": " Submit Anonymously", "value": "yes"}],
                        value=[],
                        id="anonymous",
                        switch=True,
                        className="mb-3"
                    ),

                    # 🔷 USER DETAILS
                    html.Div([
                        dbc.Label(id="label-name", className="fw-semibold"),
                        dbc.Input(id="name", className="mb-2"),

                        dbc.Label(id="label-phone", className="fw-semibold"),
                        dbc.Input(id="phone", className="mb-2"),

                        dcc.Store(id="voice-name-text"),
                    ], id="user-details-section"),

                    # 🔷 SUBMIT BUTTON (FULL WIDTH)
                    dbc.Button(
                        id="submit",
                        color="success",
                        className="w-100 mt-3",
                        style={
                            "borderRadius": "10px",
                            "fontWeight": "bold",
                            "padding": "10px"
                        }
                    ),

                    html.Br(),

                    html.Div(id="msg", className="text-center")

                ]),
                style={
                    "borderRadius": "20px",
                    "boxShadow": "0px 6px 20px rgba(0,0,0,0.1)",
                    "padding": "10px"
                }
            ),
            width=6
        ),
        justify="center"
    ),

    # 🔷 STORE
    dcc.Store(id="voice-text")

], fluid=True)
# ---------------- VOICE SCRIPT ----------------
html.Script("""
var recognition;
document.addEventListener("DOMContentLoaded", function() {
    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.lang = "en-US";

        recognition.onresult = function(event) {
            var text = event.results[0][0].transcript;
            var store = document.querySelector('#voice-text');
            if(store){
                store.value = text;
                store.dispatchEvent(new Event('input'));
            }
        };

        document.addEventListener("click", function(e) {
            if (e.target && e.target.id === "mic-btn") {
                recognition.start();
            }
        });
    }
});
""")

# ---------------- CALLBACKS ----------------
def register_callbacks(app):

    @app.callback(
        Output("user-title","children"),
        Output("label-category","children"),
        Output("label-issue","children"),
        Output("label-desc","children"),
        Output("label-name","children"),
        Output("label-phone","children"),
        Output("submit","children"),
        Output("anonymous","options"),
        Output("main-category","options"),
        Input("session","data")
    )
    def update_ui(session):
        lang = session["lang"]
        t = translations[lang]

        category_options = {
            "en": ["Harassment","Infrastructure","Discrimination","Public Safety"],
            "ta": ["தொல்லை","கட்டமைப்பு","பாகுபாடு","பாதுகாப்பு"],
            "hi": ["उत्पीड़न","बुनियादी ढांचा","भेदभाव","सुरक्षा"]
        }

        values = ["harassment","infrastructure","discrimination","safety"]

        return (
            t["title"],
            t["category"],
            t["issue"],
            t["desc"],
            t["name"],
            t["phone"],
            t["submit"],
            [{"label": t["anonymous"], "value": "yes"}],
            [{"label": category_options[lang][i], "value": values[i]} for i in range(4)]
        )

    @app.callback(
        Output("sub-category","options"),
        Input("main-category","value"),
        State("session","data")
    )
    def update_sub(main, session):
        lang = session["lang"]
        data = {
            "harassment": {
                "en": ["Verbal Abuse","Workplace Harassment"],
                "ta": ["வாய்வழி தொல்லை","பணியிடம் தொல்லை"],
                "hi": ["मौखिक उत्पीड़न","कार्यस्थल उत्पीड़न"]
            },
            "infrastructure": {
                "en": ["Bad Roads","Water Issues"],
                "ta": ["மோசமான சாலைகள்","தண்ணீர் பிரச்சனை"],
                "hi": ["खराब सड़कें","पानी की समस्या"]
            },
            "discrimination": {
                "en": ["Caste","Gender"],
                "ta": ["ஜாதி","பாலினம்"],
                "hi": ["जाति","लिंग"]
            },
            "safety": {
                "en": ["Unsafe Streets","Traffic Issues"],
                "ta": ["பாதுகாப்பற்ற சாலைகள்","போக்குவரத்து பிரச்சனை"],
                "hi": ["असुरक्षित सड़कें","यातायात समस्या"]
            }
        }
        if main in data:
            return [{"label": i, "value": i} for i in data[main][lang]]
        return []

    @app.callback(
        Output("user-details-section","style"),
        Input("anonymous","value")
    )
    def toggle_details(anon):
        if anon and "yes" in anon:
            return {"display": "none"}
        return {"display": "block"}

    @app.callback(
        Output("msg","children"),
        Input("submit","n_clicks"),
        State("main-category","value"),
        State("sub-category","value"),
        State("description","value"),
        State("anonymous","value"),
        State("name","value"),
        State("phone","value"),
        State("session","data"),
        prevent_initial_call=True
    )
    def submit(n, cat, sub, desc, anon, name, phone, session):
        lang = session["lang"]
        t = translations[lang]

        if not cat or not desc:
            return dbc.Alert(t["error"], color="danger")

        is_anon = anon and "yes" in anon
        name = "Anonymous" if is_anon else name
        phone = "N/A" if is_anon else phone
        final_category = f"{cat} - {sub}" if sub else cat

        try:
            database.insert_complaint(final_category, desc, "Yes" if is_anon else "No", name or "", phone or "")
            return dbc.Alert(f"✅ {t['success']}", color="success")
        except Exception as e:
            return dbc.Alert(f"Error: {e}", color="danger")