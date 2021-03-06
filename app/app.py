# Import dash and dash dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

# Other libs
import pandas as pd
import plotly.graph_objects as go
import argparse

# impoty layout component
from layout import layout
# Import helper functions
from analytics import totGoalsLine
from get_data import table
from analytics import playerValue

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
				external_stylesheets=external_stylesheets,
				suppress_callback_exceptions=True,
				)

app.title = "Football Stats"

app.layout = layout()

@app.callback(
    Output('stats-data', 'children'),
    [
	Input('my-input', 'value'),
	Input('button1', 'n_clicks')
	]
)
def update_output_div(input_value, n_clicks):
	"""Create statTable df and store as hidden div"""

	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	if 'button1' in changed_id:
		df = table(input_value)
		return df.to_json()

	# if n_clicks > 0:
	# 	df = table(input_value)
	# 	return df.to_json()
	
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
											'backgroundColor': 'rgb(0, 12, 39)',
											'fontWeight': 'bold'
											},
										style_cell={
													'backgroundColor': 'rgb(0, 12, 39)',
													'textAlign': 'center',
													'fontSize':15,
													'font-family':'sans-serif'
													}
										)
									)
	else:
		return dash.no_update


@app.callback(
	Output('totgoals', 'figure'),
	[Input('stats-data', 'children'),
	Input('dropdown', 'value')
	]
)
def goalsLine(json_df, dropdownVal):
	fig = go.Figure()

	if json_df:
		df = pd.read_json(json_df)
		fig = totGoalsLine(df, dropdownVal)
		return fig
	else:
		return dash.no_update

@app.callback(
	Output('player-val', 'children'),
	[Input('my-input', 'value')]
)
def playerName(name):
	# convert to Proper Case
	name = name.title()
	if name:
		value = playerValue(name)
		# if player value doesnt exist, do nothing
		if value.empty:
			pass
		else:
			return html.Div([
					html.Span([html.Div("Player Value: "), html.Div(value)])
				], className='row')
	else:
		return dash.no_update

if __name__ == '__main__':
	app.run_server(host='0.0.0.0', debug=True, port=8050)
