import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read data
df = pd.read_csv("formatted_sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div(
    style={"padding": "30px"},
    children=[
        html.H1(
            "Pink Morsel Sales Visualizer",
            style={"textAlign": "center"}
        ),

        html.Div([
            html.Label(
                "Select Region:",
                style={
                    "fontWeight": "bold",
                    "fontSize": "18px"
                }
            ),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True,
                style={"marginBottom": "20px"}
            )
        ]),

        dcc.Graph(id="sales-chart")
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[
            filtered_df["Region"].str.lower() == selected_region
        ]

    daily_sales = (
        filtered_df
        .groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f9",
        font=dict(size=14)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)