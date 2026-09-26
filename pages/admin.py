import dash
from dash import html, Output, Input, dash_table
import dash_bootstrap_components as dbc
import database  # our fixed database.py

# ---------------- Dash App ----------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], suppress_callback_exceptions=True)

# ---------------- Admin Layout ----------------
admin_layout = dbc.Container([

    html.H2("Admin Dashboard", className="text-center mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Complaints"), html.H3(id="total")])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5("Harassment"), html.H3(id="harassment")])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5("Infrastructure"), html.H3(id="infra")])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5("Discrimination"), html.H3(id="discrimination")])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5("Safety"), html.H3(id="safety")])), width=2),
    ], className="mb-4"),

    html.H4("All Complaints", className="mt-3"),
    html.Div(id="table")

], fluid=True)

# ---------------- Admin Callback ----------------
@app.callback(
    Output("total", "children"),
    Output("harassment", "children"),
    Output("infra", "children"),
    Output("discrimination", "children"),
    Output("safety", "children"),
    Output("table", "children"),
    Input("total", "id")  # dummy input to trigger on page load
)
def update_admin_dashboard(_):
    df = database.get_all_complaints()

    total = len(df)
    harassment = len(df[df['category'].str.contains("harassment", case=False, na=False)])
    infra = len(df[df['category'].str.contains("infrastructure", case=False, na=False)])
    discrimination = len(df[df['category'].str.contains("discrimination", case=False, na=False)])
    safety = len(df[df['category'].str.contains("safety", case=False, na=False)])

    # Complaints Table
    if not df.empty:
        table = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            style_table={'overflowX': 'auto'},
            page_size=10,
            style_cell={'textAlign': 'left'}
        )
    else:
        table = html.P("No complaints yet.")

    return total, harassment, infra, discrimination, safety, table

# ---------------- Run Server ----------------
if __name__ == "__main__":
    app.run_server(debug=True)