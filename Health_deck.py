
import streamlit as st
import pandas as pd
import numpy as np

st.title('HealthAura: Pro Sports Tracker')

# Dictionaries for teams by sport
teams_by_sport = {
    'NFL': [
        'Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills',
        'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns',
        'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers',
        'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs',
        'Las Vegas Raiders', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins',
        'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants',
        'New York Jets', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers',
        'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Commanders'
    ],
    'NBA': [
        'Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets',
        'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets',
        'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers',
        'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat',
        'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks',
        'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns',
        'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors',
        'Utah Jazz', 'Washington Wizards'
    ],
    'NHL': [
        'Anaheim Ducks', 'Arizona Coyotes', 'Boston Bruins', 'Buffalo Sabres',
        'Calgary Flames', 'Carolina Hurricanes', 'Chicago Blackhawks', 'Colorado Avalanche',
        'Columbus Blue Jackets', 'Dallas Stars', 'Detroit Red Wings', 'Edmonton Oilers',
        'Florida Panthers', 'Los Angeles Kings', 'Minnesota Wild', 'Montreal Canadiens',
        'Nashville Predators', 'New Jersey Devils', 'New York Islanders', 'New York Rangers',
        'Ottawa Senators', 'Philadelphia Flyers', 'Pittsburgh Penguins', 'San Jose Sharks',
        'Seattle Kraken', 'St. Louis Blues', 'Tampa Bay Lightning', 'Toronto Maple Leafs',
        'Vancouver Canucks', 'Vegas Golden Knights', 'Washington Capitals', 'Winnipeg Jets'
    ],
    'MLB': [
        'Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox',
        'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Guardians',
        'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals',
        'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers',
        'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics',
        'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'San Francisco Giants',
        'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers',
        'Toronto Blue Jays', 'Washington Nationals'
    ]
}

# Mapping of leagues to their respective raw GitHub CSV file URLs
roster_urls = {
    'MLB': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Roster.csv',
    'NBA': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Roster.csv',
    'NFL': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Roster.csv',
    'NHL': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Roster.csv',
}

def load_roster_data(league):
    """Load roster data from a CSV file hosted on GitHub."""
    url = roster_urls.get(league)
    if url:
        df = pd.read_csv(url)
        return df
    else:
        st.error(f"No URL found for the league: {league}")
        return pd.DataFrame()

st.title('Sports Rosters')

# User selects a league
league_selection = st.sidebar.selectbox('Select a League', ['Select a league'] + list(roster_urls.keys()))

if league_selection != 'Select a league':
    # Load the roster data for the selected league
    roster_df = load_roster_data(league_selection)
    
    if not roster_df.empty:
        # Assuming there's a 'Team' column in your CSV files
        team_selection = st.sidebar.selectbox('Select a Team', ['Select a team'] + sorted(roster_df['Team'].unique()))
        
        if team_selection != 'Select a team':
            # Filter the DataFrame for the selected team
            team_df = roster_df[roster_df['Team'] == team_selection]
            
            # Display the roster for the selected team
            st.write(f'Roster for {team_selection}:')
            st.dataframe(team_df[['Name', 'Pos', 'Ht', 'WT', 'Age', 'Yrs of EXP']], width=800)


# Selectbox for sports
sports_options = ['Select a sport', 'NFL', 'NBA', 'NHL', 'MLB']
sport_choice = st.sidebar.selectbox('Sports', sports_options)

if sport_choice != 'Select a sport':
    # Teams dropdown based on sport selected
    teams_options = ['All teams'] + teams_by_sport[sport_choice]
    team_choice = st.sidebar.selectbox('Teams', teams_options)
    
    # Organization dropdown placeholder, you will need to populate it similar to the previous example
    organization_options = ['Select organization', 'Alphabetical', 'By Position', 'By Seasonal Health', 'By Career Health', 'By Percent of Reinjury', 'By Injury Date', 'By Agent']
    organization_choice = st.sidebar.selectbox('Organize Data By', organization_options)
    
    # Display selections
    st.write(f'Sport selected: {sport_choice}')
    st.write(f'Team selected: {team_choice}')
    st.write(f'Organization selected: {organization_choice}')
    
    # Here, you would include your logic to filter and display the data based on the selections
else:
    st.write("Please select a sport to view and organize data.")


# Assuming `df` is your main DataFrame containing all the player, team, and injury data

# Sample structure for df
data = {
    'Team Name': [],
    'Player Name': [],
    'Career Health': [],
    'Seasonal Health': [],
    'Percent of Injury': [],
    'Position': [],
    'Height': [],
    'Weight': [],
    'Age': [],
    'Years of Experience': [],
    'Agent': [],
    'Agent Email': [],
    'Agency': [],
    # Assume there's also injury history data in this DataFrame
}



