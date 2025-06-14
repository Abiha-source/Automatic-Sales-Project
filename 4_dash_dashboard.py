# Dash Dashboard

import dash
from dash import html, dcc

app = dash.Dash(__name__)
app.title = 'XYZAutomotives Dashboard'

app.layout = html.Div([
    html.H1('XYZAutomotives Dashboard'),
    html.P('This dashboard displays sales and economic trends.')
])

if __name__ == '__main__':
    app.run(port=8051)
# 5. Plotly Dash Dashboard

```python
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv("cleaned_automobile_sales.csv")
df['year'] = pd.DatetimeIndex(df['date']).year

# Initialize app
app = dash.Dash(__name__)
app.title = "Automobile Sales Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Automobile Sales Dashboard", style={'textAlign': 'center'}),

    html.Label("Select Vehicle Type:"),
    dcc.Dropdown(
        id='vehicle-dropdown',
        options=[{'label': vt, 'value': vt} for vt in df['vehicle_type'].unique()],
        value=df['vehicle_type'].unique()[0]
    ),

    dcc.Graph(id='sales-line-plot'),
    html.Div(id='output-div', className='output-style')
])

# Callback to update plot
@app.callback(
    Output('sales-line-plot', 'figure'),
    Input('vehicle-dropdown', 'value')
)
def update_graph(selected_vehicle):
    filtered_df = df[df['vehicle_type'] == selected_vehicle]
    grouped = filtered_df.groupby('year')['automobile_sales'].sum().reset_index()
    fig = px.line(grouped, x='year', y='automobile_sales', title=f"Yearly Sales for {selected_vehicle}")
    return fig

# Run the app (if you want to run this file directly)
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050)
```

This script:
- Builds a simple dashboard with dropdown filtering
- Displays yearly sales trend for selected vehicle type
- Requires running as a standalone app

