# Make a script that scrapes wikipedia player stats
# returns goals scored, and some info

from bs4 import BeautifulSoup
import requests
import pandas as pd
import wikipedia as wiki


import numpy as np
import lxml
import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import html5lib

# import seaborn as sns

# from matplotlib import style
# import matplotlib as mpl
# import matplotlib.pyplot as plt



# player = "Eden Hazard"
# url = wiki.page(player)
# title = url.title
# summary = url.summary
# print(summary)

# Scrape Player Wikipedia Site
# player_name = "Eden Hazard"

def player_page(player_name):
	player_name1 = player_name.replace(" ", "_")
	# convert to Proper Case
	player_name1 = player_name1.title()

	# Using url
	url = "https://en.wikipedia.org/wiki/" + player_name1

	# open url with urllib.request
	page = urllib.request.urlopen(url)

	soup = BeautifulSoup(page, "lxml")

	return soup

def table(player):

    soup = player_page(player)

    # Club stats section
    heading = soup.find(id='Club')
    statTable = heading.find_next('table', class_='wikitable')
    statTable = pd.read_html(str(statTable))[0]
    statTable.columns = ['_'.join(x) for x in statTable.columns]

    statTable.iloc[:,2: ] = statTable.iloc[:,2: ].apply(pd.to_numeric, errors='ignore')

    # Only keep final total col
    statTable = statTable[~statTable.Season_Season.str.contains('Total')]
	# print(statTable)
    return statTable











