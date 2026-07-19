import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read the processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")

# Group sales by date
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualizer",
        style={"textAlign": "center"}
    ),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)