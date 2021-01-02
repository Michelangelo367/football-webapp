import dash_html_components as html
import dash_core_components as dcc


def layout() -> html.Div:
    """
    Returns the main html div element for the app
    """
    layout = html.Div([

        # navbar
        html.Div(
            html.Div(
                html.H5("⚽ Football Stats Dashboard"),
                className="navbar-text"),
                className="navbar"),

        # Body
        html.Div([

        html.H6("Enter the name of a player"),
        html.Div([
            html.Div([
            html.Div(
                [dcc.Input(id='my-input',
                            value='Eden Hazard', type='text')
                ], className='button1'),
            html.Div(html.Button('Submit', id='button1', n_clicks=0)),
            ],className='two columns'),
            html.Div([
                dcc.Dropdown(
                    id="dropdown",
                    options=[
                        {'label': 'Goals', 'value': 'Goals'},
                        # {'label': 'Assists', 'value': 'Assists'},
                        {'label': 'Games Played', 'value': 'Games Played'}
                    ],
                    value='Games Played',
                    clearable=False
                )
            ], className='two columns')
        ],className='row'),
        html.Br(),
        html.Div(id="player-val"),
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

        ],className='main-body')

    ])


    return layout
