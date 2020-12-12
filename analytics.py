# Create some analytics from the goal stats
import pandas as pd
from get_data import table
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def sumStats(playerName):
	statTable = table(playerName)

	return statTable


def totGoalsLine(statTable):
	y = statTable['Total_Goals'].iloc[:-2]
	x = statTable['Season_Season'].iloc[:-2].drop_duplicates()
	
	# Goals to games ratio
	totGames = int(statTable['Total_Apps'].tail(1))
	totGoals = int(statTable['Total_Goals'].tail(1))
	goalGames = round(totGoals/totGames,2)

	totGamesL = int(statTable['League_Apps'].iloc[-1])
	totGoalsL = int(statTable['League_Goals'].iloc[-1])
	goalGamesL = round(totGoalsL/totGamesL,2)

	goalGames = round(totGoals/totGames,2)
	goalPerGame = pd.DataFrame(statTable['Season_Season'].iloc[:-2].drop_duplicates())
	goalPerGame['Goals per Game'] = goalGames
	fig = make_subplots(specs=[[{"secondary_y": True}]])

	fig.add_trace(
			go.Bar(
			y=y,
			x=x,
			name="Goals per Season"   
			)
		)

	fig.add_trace(
		go.Scatter(y=goalPerGame['Goals per Game'],
				x=x,
				name="Goals per Game"
				),
			secondary_y=True,
	)

	fig.update_layout(
		title='Total Goals per Season',
		xaxis_title="Season",
		yaxis_title="Goals per Season",
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
# - goals per game
# - goals per game per competition plots