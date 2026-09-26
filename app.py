# ACCESS-ENG MULTILINGUAL APP (FINAL FIXED)
print("🔥 THIS FILE IS RUNNING 🔥")
from pydoc import text

import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import database
import guidance


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)
app.clientside_callback(
    """
    function(n_clicks) {
        if (!n_clicks) return "";

        var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) return "";

        var recognition = new SpeechRecognition();
        recognition.lang = "en-IN";

        recognition.start();

        document.getElementById("voice-status").innerText = "🎙 Listening...";

        return new Promise((resolve) => {
            recognition.onresult = function(event) {
                var text = event.results[0][0].transcript;
                document.getElementById("voice-status").innerText = "✅ Done";
                resolve(text);
            };

            recognition.onerror = function() {
                document.getElementById("voice-status").innerText = "❌ Error";
                resolve("");
            };
        });
    }
    """,
    Output("voice-text", "data"),
    Input("mic-btn", "n_clicks")
)
app.clientside_callback(
    """
    function(n_clicks) {
        if (!n_clicks) return "";

        var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) return "";

        var recognition = new SpeechRecognition();
        recognition.lang = "en-IN";

        recognition.start();

        document.getElementById("voice-name-status").innerText = "🎙 Listening...";

        return new Promise((resolve) => {
            recognition.onresult = function(event) {
                var text = event.results[0][0].transcript;
                document.getElementById("voice-name-status").innerText = "✅ Done";
                resolve(text);
            };

            recognition.onerror = function() {
                document.getElementById("voice-name-status").innerText = "❌ Error";
                resolve("");
            };
        });
    }
    """,
    Output("voice-name-text", "data"),
    Input("mic-name-btn", "n_clicks")
)

# ----------------- TRANSLATIONS -----------------
translations = {
    "en": {
        "login": "ACCESS-ENG Login",
        "select_lang": "Select Language",
        "role": "Select Role",
        "user": "User",
        "admin_role": "Admin",
        "password": "Password ",
        "login_btn": "Login",
        "user_portal": "User Complaint Portal",
        "category": "Select Category",
        "issue": "Select Issue",
        "other": "If Other, specify",
        "desc": "Detailed Description",
        "anonymous": "Submit Anonymously",
        "name": "Name",
        "phone": "Contact Number",
        "submit": "Submit",
        "success": "Complaint submitted successfully!",
        "error": "Please fill all required fields",
        "admin": "Admin Dashboard",
        "total": "Total Complaints"
    },
    "ta": {
        "login": "ACCESS-ENG உள்நுழைவு",
        "select_lang": "மொழியை தேர்ந்தெடுக்கவும்",
        "role": "பாத்திரத்தை தேர்ந்தெடுக்கவும்",
        "user": "பயனர்",
        "admin_role": "நிர்வாகி",
        "password": "கடவுச்சொல்",
        "login_btn": "உள்நுழைய",
        "user_portal": "புகார் பதிவு மையம்",
        "category": "வகையை தேர்ந்தெடுக்கவும்",
        "issue": "பிரச்சினையை தேர்ந்தெடுக்கவும்",
        "other": "வேறு இருந்தால் குறிப்பிடவும்",
        "desc": "விவரம்",
        "anonymous": "அடையாளம் தெரியாமல்",
        "name": "பெயர்",
        "phone": "தொலைபேசி எண்",
        "submit": "சமர்ப்பிக்கவும்",
        "success": "புகார் வெற்றிகரமாக சமர்ப்பிக்கப்பட்டது!",
        "error": "தேவையான தகவல்களை நிரப்பவும்",
        "admin": "நிர்வாக பலகை",
        "total": "மொத்த புகார்கள்"
    },
    "hi": {
        "login": "ACCESS-ENG लॉगिन",
        "select_lang": "भाषा चुनें",
        "role": "भूमिका चुनें",
        "user": "उपयोगकर्ता",
        "admin_role": "प्रशासक",
        "password": "पासवर्ड",
        "login_btn": "लॉगिन", 
        "user_portal": "शिकायत पोर्टल",
        "category": "श्रेणी चुनें",
        "issue": "समस्या चुनें",
        "other": "अन्य हो तो लिखें",
        "desc": "विवरण",
        "anonymous": "गुमनाम",
        "name": "नाम",
        "phone": "फोन नंबर",
        "submit": "जमा करें",
        "success": "शिकायत सफलतापूर्वक जमा हुई!",
        "error": "सभी आवश्यक जानकारी भरें",
        "admin": "एडमिन डैशबोर्ड",
        "total": "कुल शिकायतें"
    }
}

# ----------------- LOGIN LAYOUT -----------------
login_layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody([

                    html.H2(id="login-title", className="text-center mb-4"),

                    dbc.Label(id="label-lang"),
                    dcc.Dropdown(
                        id="login-language",
                        options=[
                            {"label": "English", "value": "en"},
                            {"label": "தமிழ்", "value": "ta"},
                            {"label": "हिन्दी", "value": "hi"}
                        ],
                        value="en",
                        clearable=False
                    ),

                    html.Br(),

                    dbc.Label(id="label-role"),
                    dcc.Dropdown(id="role"),

                    html.Br(),

                    html.Div([
                        dbc.Label(id="label-password"),
                        dbc.Input(id="password", type="password"),
                    ], id="password-box", style={"display": "none"}),

                    html.Br(),

                    dbc.Button(id="login-btn", color="primary", className="w-100"),

                    html.Br(), html.Br(),

                    html.Div(id="login-msg", className="text-center")

                ]),
                style={
                    "borderRadius": "20px",
                    "boxShadow": "0px 8px 25px rgba(0,0,0,0.15)"
                }
            ),
            width=4
        ),
        justify="center",
        align="center",
        className="vh-100"
    ),
    fluid=True
)

# ----------------- LOGIN TEXT + ROLE OPTIONS -----------------
@app.callback(
    Output("login-title","children"),
    Output("label-lang","children"),
    Output("label-role","children"),
    Output("label-password","children"),
    Output("login-btn","children"),
    Output("role","options"),   # ✅ THIS IS THE REAL FIX
    Input("login-language","value")
)
def update_login(lang):
    t = translations[lang]

    return (
        t["login"],
        t["select_lang"],
        t["role"],          # label for role
        t["password"],      # label for password
        t["login_btn"],
        [
            {"label": t["user"], "value": "user"},
            {"label": t["admin_role"], "value": "admin"}
        ]
    )
# ----------------- PASSWORD BOX SHOW/HIDE -----------------
@app.callback(
    Output("password-box", "style"),
    Input("role", "value")
)
def toggle_password(role):
    if role == "admin":
        return {"display": "block"}
    return {"display": "none"}

# ----------------- USER -----------------
user_layout = dbc.Container([
    html.H2(id="user-title", className="text-center mb-4"),

    dbc.Card(dbc.CardBody([

        # 🔷 CATEGORY
        dbc.Label(id="label-category"),
        dcc.Dropdown(id="main-category"),

        html.Br(),

        # 🔷 GUIDANCE (CORRECT PLACE ✅)
        html.Div(id="guidance-box"),

        html.Br(),

        # 🔷 SUB CATEGORY
        dbc.Label(id="label-issue"),
        dcc.Dropdown(id="sub-category"),

        html.Br(),

       

        # 🔷 DESCRIPTION
        dbc.Label(id="label-desc"),
        dbc.Textarea(id="description"),
        

        html.Br(),

        html.Button("🎤 Speak", id="mic-btn", n_clicks=0),

        html.Div(id="voice-status"),

        dcc.Store(id="voice-text"),

        html.Br(),

        # 🔷 ANONYMOUS
        dbc.Checklist(
            id="anonymous",
            options=[{"label": "", "value": "yes"}],
            value=[],
            switch=True
        ),

        html.Br(),

        # 🔷 USER DETAILS
        html.Div([
            dbc.Label(id="label-name"),
            dbc.Input(id="name"),
            html.Button("🎤 Speak Name", id="mic-name-btn", n_clicks=0),
            html.Div(id="voice-name-status"),
            dcc.Store(id="voice-name-text"),
            html.Br(),
            dbc.Label(id="label-phone"),
            dbc.Input(id="phone")
        ], id="user-details-section"),

        html.Br(),

        # 🔷 SUBMIT
        dbc.Button(
    id="submit-btn",
    color="success",
    className="w-100",
    style={"borderRadius": "10px", "fontWeight": "bold"}
   ),

        html.Br(), html.Br(),

        html.Div(id="msg")

    ]))
], fluid=True)

# ----------------- ADMIN -----------------
admin_layout = dbc.Container([

    html.H2("Admin Dashboard", className="text-center mb-4"),

    # 🔷 STATS CARDS
    dbc.Row([

        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H5("Total Complaints"),
                html.H3(id="total")
            ])),
            width=2
        ),

        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H5("Harassment"),
                html.H3(id="harassment")
            ])),
            width=2
        ),

        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H5("Infrastructure"),
                html.H3(id="infra")
            ])),
            width=2
        ),

        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H5("Discrimination"),
                html.H3(id="discrimination")
            ])),
            width=2
        ),

        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H5("Safety"),
                html.H3(id="safety")
            ])),
            width=2
        ),

    ], className="mb-4"),

    # 🔷 TABLE
    html.H4("All Complaints", className="mt-3"),
    html.Div(id="table")

], fluid=True)

# ----------------- APP LAYOUT -----------------
app.layout = dbc.Container([
    dcc.Location(id="url"),
    dcc.Store(id="session"),
    html.Div(id="page-content")
])

@app.callback(
    Output("description", "value"),
    Input("voice-text", "data"),
    prevent_initial_call=True
)
def fill_text(data):
    return data if data else dash.no_update 

@app.callback(
    Output("name", "value"),
    Input("voice-name-text", "data"),
    prevent_initial_call=True
)
def fill_name(data):
    return data if data else dash.no_update

# ----------------- ROUTER -----------------
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    State("session", "data")
)
def route(path, session):
    if not session or "role" not in session:
        return login_layout
    if path == "/admin" and session["role"] == "admin":
        return admin_layout
    return user_layout

# ----------------- LOGIN -----------------
@app.callback(
    Output("session", "data"),
    Output("url", "pathname"),
    Output("login-msg", "children"),
    Input("login-btn", "n_clicks"),
    State("role", "value"),
    State("password", "value"),
    State("login-language", "value"),
    prevent_initial_call=True
)
def login(n, role, password, lang):

    if not role:
        return dash.no_update, dash.no_update, ""

    if role == "admin":
        if password != "admin123":
            return dash.no_update, dash.no_update, "❌ Wrong password"
        return {"role": "admin", "lang": lang}, "/admin", "✅ Login successful"

    return {"role": "user", "lang": lang}, "/", "✅ Login successful"


# ----------------- LOGIN TEXT -----------------
# ----------------- USER TEXT + CATEGORY -----------------
@app.callback(
    Output("user-title","children"),
    Output("label-category","children"),
    Output("label-issue","children"),
    Output("label-desc","children"),
    Output("label-name","children"),
    Output("label-phone","children"),
    Output("submit-btn","children"),
    Output("anonymous","options"),
    Output("main-category","options"),
    Input("session","data")
)
def update_user(session):

    if not session:
        return [""] * 9   # prevents crash

    lang = session.get("lang", "en")
    t = translations[lang]

    labels = {
        "en": ["Harassment","Infrastructure","Discrimination","Public Safety"],
        "ta": ["தொல்லை","கட்டமைப்பு","பாகுபாடு","பாதுகாப்பு"],
        "hi": ["उत्पीड़न","बुनियादी ढांचा","भेदभाव","सुरक्षा"]
    }

    values = ["harassment","infrastructure","discrimination","safety"]

    return (
    t["user_portal"],
    t["category"],
    t["issue"],
    t["desc"],
    t["name"],
    t["phone"],
    t["submit"],
    [{"label": t["anonymous"], "value": "yes"}],
    [{"label": labels[lang][i], "value": values[i]} for i in range(4)]
)
# ----------------- SUB CATEGORY -----------------
@app.callback(
    Output("sub-category", "options"),
    Input("main-category", "value"),
    State("session", "data")
)
def update_sub(main, session):

    if not session:
        return []

    lang = session.get("lang", "en")

    data = {
        "harassment": {
            "en": [
                ("Verbal Abuse","verbal"),
                ("Workplace Harassment","workplace"),
                ("Cyberbullying","cyber"),
                ("Stalking","stalking"),
                ("Sexual Harassment","sexual")
            ],
            "ta": [
                ("வாய்வழி தொல்லை","verbal"),
                ("பணியிடம் தொல்லை","workplace"),
                ("இணைய துன்புறுத்தல்","cyber"),
                ("பின்தொடர்தல்","stalking"),
                ("பாலியல் தொல்லை","sexual")
            ],
            "hi": [
                ("मौखिक उत्पीड़न","verbal"),
                ("कार्यस्थल उत्पीड़न","workplace"),
                ("साइबर बुलिंग","cyber"),
                ("पीछा करना","stalking"),
                ("यौन उत्पीड़न","sexual")
            ]
        },

        "infrastructure": {
            "en": [
                ("Bad Roads","roads"),
                ("Water Issues","water"),
                ("Electricity Problems","electricity"),
                ("Garbage Issues","garbage"),
                ("Transport Issues","transport")
            ],
            "ta": [
                ("மோசமான சாலைகள்","roads"),
                ("தண்ணீர் பிரச்சனை","water"),
                ("மின்சாரம் பிரச்சனை","electricity"),
                ("குப்பை பிரச்சனை","garbage"),
                ("போக்குவரத்து பிரச்சனை","transport")
            ],
            "hi": [
                ("खराब सड़कें","roads"),
                ("पानी की समस्या","water"),
                ("बिजली समस्या","electricity"),
                ("कचरा समस्या","garbage"),
                ("परिवहन समस्या","transport")
            ]
        },

        "discrimination": {
            "en": [
                ("Caste","caste"),
                ("Gender","gender"),
                ("Religious","religion"),
                ("Workplace Bias","bias"),
                ("Denial of Services","denial")
            ],
            "ta": [
                ("சாதி","caste"),
                ("பாலினம்","gender"),
                ("மதம்","religion"),
                ("பணியிடம் பாகுபாடு","bias"),
                ("சேவை மறுப்பு","denial")
            ],
            "hi": [
                ("जाति","caste"),
                ("लिंग","gender"),
                ("धर्म","religion"),
                ("कार्यस्थल पक्षपात","bias"),
                ("सेवा से इंकार","denial")
            ]
        },

        "safety": {
            "en": [
                ("Unsafe Streets","lighting"),
                ("Crime Area","crime"),
                ("Traffic Issues","traffic"),
                ("Emergency Delay","emergency"),
                ("Unsafe Spaces","unsafe")
            ],
            "ta": [
                ("பாதுகாப்பற்ற தெருக்கள்","lighting"),
                ("குற்றப்பகுதி","crime"),
                ("போக்குவரத்து பிரச்சனை","traffic"),
                ("அவசர தாமதம்","emergency"),
                ("பாதுகாப்பற்ற இடங்கள்","unsafe")
            ],
            "hi": [
                ("असुरक्षित सड़कें","lighting"),
                ("अपराध क्षेत्र","crime"),
                ("ट्रैफिक समस्या","traffic"),
                ("आपातकालीन देरी","emergency"),
                ("असुरक्षित स्थान","unsafe")
            ]
        }
    }

    if main in data:
        return [
            {"label": label, "value": value}
            for label, value in data[main][lang]
        ]

    return []

# ----------------- SHOW/HIDE NAME -----------------
@app.callback(
    Output("user-details-section","style"),
    Input("anonymous","value")
)
def toggle_details(anon):
    if anon and "yes" in anon:
        return {"display": "none"}
    return {"display": "block"} 

# ----------------- SUBMIT -----------------
@app.callback(
    Output("msg","children"),
    Input("submit-btn","n_clicks"),
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

    lang=session.get("lang", "en")
    t = translations[lang]

    if not cat or not desc:
        return dbc.Alert(t["error"], color="danger")

    is_anon = anon and "yes" in anon

    if is_anon:
        name, phone = "Anonymous", "N/A"

    try:
        database.insert_complaint(cat, desc, "Yes" if is_anon else "No", name or "", phone or "")
        return dbc.Alert(f"✅ {t['success']}", color="success")
    except Exception as e:
        return dbc.Alert(f"Error: {e}", color="danger")

# ----------------- ADMIN TEXT -----------------
@app.callback(
    Output("total", "children"),
    Output("harassment", "children"),
    Output("infra", "children"),
    Output("discrimination", "children"),
    Output("safety", "children"),
    Output("table", "children"),
    Input("total", "id")
)
def update_admin(_):

    df = database.get_all_complaints()

    total = len(df)

    harassment = len(df[df['category'].str.contains("harassment", case=False, na=False)])
    infra = len(df[df['category'].str.contains("infrastructure", case=False, na=False)])
    discrimination = len(df[df['category'].str.contains("discrimination", case=False, na=False)])
    safety = len(df[df['category'].str.contains("safety", case=False, na=False)])

    if not df.empty:
        table = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'}
        )
    else:
        table = "No complaints yet"

    return total, harassment, infra, discrimination, safety, table 

@app.callback(
    Output("guidance-box", "children"),
    Input("main-category", "value"),
    State("session", "data")
)

def show_guidance(category, session):

    if not category or not session:
        return ""

    lang = session.get("lang", "en")

    g = guidance.get_guidance(category, lang)

    return dbc.Card(dbc.CardBody([
        html.H5(g.get("title")),

        html.B("Steps:"),
        html.Ul([html.Li(i) for i in g.get("steps", [])]),

        html.B("Laws:"),
        html.Ul([html.Li(i) for i in g.get("laws", [])]),

        html.B("Helpline:"),
        html.Ul([html.Li(i) for i in g.get("helpline", [])])
    ]), className="mb-3")


# ----------------- RUN -----------------
if __name__ == "__main__":
    app.run(debug=False, port=8051)