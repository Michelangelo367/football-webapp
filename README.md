# Football Stats Web App

A simple dashboard that lets you search for basic statistics for a given player, like goals scored per season, number of appearences per season, and goals per game over time.

![Alt text](app/assets/footballappscrn.png?raw=true "Title")

## Run App
```shell
git clone https://github.com/sele14/football-webapp.git
cd football-webapp/

# Build docker image
docker build -t football-app
# Run
docker run -p 8050:8050 football-app
```


## Developing

### Built With
Python, Pandas, and Plotly Dash.

### Setting up Dev*

```shell
git clone https://github.com/sele14/football-webapp.git
cd football-webapp/

# Set up virtual env
py -m venv venv
.\venv\Scripts\activate

# install depends
py -m pip install -r requirements.txt

# Run development server
py app/app.py
```

### * Note: replace 'py' with 'python3' or equivalent for your operating system and setup.