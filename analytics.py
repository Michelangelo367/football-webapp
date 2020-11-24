# Create some analytics from the goal stats
import pandas as pd
from get_data import table
import plotly.graph_objects as go


def sumStats(playerName):
	statTable = table(playerName)

	# Goals to games ratio
	totGames = int(statTable['Total_Apps'].tail(1))
	totGoals = int(statTable['Total_Goals'].tail(1))
	goalGames = round(totGoals/totGames,2)

	totGamesL = int(statTable['League_Apps'].iloc[-1])
	totGoalsL = int(statTable['League_Goals'].iloc[-1])
	goalGamesL = round(totGoalsL/totGamesL,2)


def totGoalsLine(statTable):
	y = statTable['Total_Goals'].iloc[:-2]
	x = statTable['Season_Season'].iloc[:-2]

	fig = go.Figure(
		data=go.Scatter(
			y=y,
			x=x
			)
		)

	fig.update_layout(
		title='Total Goals per Season',
		xaxis_title="Season",
		yaxis_title="Goals",
		font_color="white",
		plot_bgcolor='rgb(0, 12, 39)',
		paper_bgcolor='rgb(0, 12, 39)',
		xaxis =  {'showgrid': False},
        yaxis = {'showgrid': False}
		)

	return fig



# Next:
# See e.g. https://www.dataskunkworks.com/latest-posts/wikipedia-scraping-2020


# Analytics;
# - sumstats
# - trend over time of games played, goals scored plots
# - goals per game
# - goals per game per competition plots