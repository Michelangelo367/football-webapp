# Make a script that scrapes wikipedia player stats
# returns goals scored, and some info

from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import wikipedia as wiki
import lxml
import urllib.request

def _player_page(player_name: str) -> DataFrame:
    
	player_name1 = player_name.replace(" ", "_")
	# convert to Proper Case
	player_name1 = player_name1.title()

	# Get player wikipedia page
	url = "https://en.wikipedia.org/wiki/" + player_name1

	# open url with urllib.request
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, "lxml")

	return soup

def table(player: str) -> DataFrame:
    """
    Get player stats table from wikipedia.
    Input: Player name
    Output: a dataframe
    """

    soup = _player_page(player)

    # Club stats section
    heading = soup.find(id='Club')
    statTable = heading.find_next('table', class_='wikitable')
    statTable = pd.read_html(str(statTable))[0]
    statTable.columns = ['_'.join(x) for x in statTable.columns]

    statTable.iloc[:,2: ] = statTable.iloc[:,2: ].apply(pd.to_numeric, errors='ignore')

    # Only keep final total col
    statTable = statTable[~statTable.Season_Season.str.contains('Total')]

    return statTable











