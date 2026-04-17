import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.H1("Pink Morsel Sales Dashboard", style={
        "textAlign": "center",
        "color": "#ff69b4"
    }),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "North"},
            {"label": "East", "value": "East"},
            {"label": "South", "value": "South"},
            {"label": "West", "value": "West"},
        ],
        value="all",
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-graph")

], style={
    "backgroundColor": "#fce4ec",
    "padding": "20px"
})

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    filtered_df = filtered_df.sort_values("Date")

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Sales Over Time"
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
