import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from get_data import table
import dash_table
import pandas as pd
import plotly.graph_objects as go

# Module
from analytics import sumStats, totGoalsLine

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
				external_stylesheets=external_stylesheets,
				suppress_callback_exceptions=True,

				)

app.layout = html.Div([
    html.H6("Enter the name of a player"),
	html.Div([
		html.Div(
			[dcc.Input(id='my-input',
						value='Eden Hazard', type='text')
			], className='button1'),
		html.Div(html.Button('Submit', id='button1', n_clicks=0))
	],className='row'),
    html.Br(),
	# Goals Graph
	html.Div(
		dcc.Graph(
			id='totgoals',
			figure={
				'layout': {
                'plot_bgcolor': 'rgb(0, 12, 39)',
				'paper_bgcolor': 'rgb(0, 12, 39)',
				}
			}

			),style={'backgroundColor' : 'rgb(0, 12, 39)'}
	),

	# Table
    html.Div(id='my-output'),

	# Store data as hidden div (or dcc.Store?)
	html.Div(id='stats-data', 
			style={"display" : 'none'}
			)

])


@app.callback(
    Output('stats-data', 'children'),
    [
	Input('my-input', 'value'),
	Input('button1', 'n_clicks')
	]
)
def update_output_div(input_value, n_clicks):
	# Create statTable df and store as hidden div
	if n_clicks >= 1:
		df = table(input_value)
		return df.to_json()
	else:
		return dash.no_update


@app.callback(
	Output('my-output', 'children'),
	[Input('stats-data', 'children')]
)
def goals_table(json_df):
	if json_df:
		df = pd.read_json(json_df)
		return html.Div(dash_table.DataTable(
										data=df.to_dict('records'),
										id='table',
										columns=[
											{'name': i, 
											'id': i,
											'selectable' : True,
											'hideable' : True,
											'selectable': True}
											for i in df.columns
											],
										sort_action="native",
										filter_action='native',
										sort_mode='multi',
										page_current = 0,
										page_size = 10,
										style_table={'overflowX': 'scroll'},
										style_as_list_view=True,
										style_header={
											'backgroundColor': 'rgb(21, 32, 58)',
											'fontWeight': 'bold'
											},
										style_cell={
													'backgroundColor': 'rgb(21, 32, 58)',
													'textAlign': 'center',
													'fontSize':15,
													'font-family':'sans-serif'
													}
										)
									)

@app.callback(
	Output('totgoals', 'figure'),
	[Input('stats-data', 'children')]
)
def goalsLine(json_df):
	fig = go.Figure()

	if json_df:
		df = pd.read_json(json_df)
		fig = totGoalsLine(df)
		return fig



if __name__ == '__main__':
    app.run_server(debug=True)
