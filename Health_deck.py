import streamlit as st
import pandas as pd
import numpy as np

st.title('HealthAura: Pro Sports Tracker')

# Updated dictionary for NFL teams with their respective GitHub raw CSV file URLs
team_roster_urls = 
    'NFL': {
        'Arizona Cardinals': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Arizona%20Cardinals%20Roster.csv',
        'Atlanta Falcons': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Atlanta%20Falcons.csv',
        'Baltimore Ravens': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Baltimore%20Ravens.csv',
        'Buffalo Bills': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Buffalo%20Bills.csv',
        'Carolina Panthers': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Carolina%20Panthers.csv',
        'Chicago Bears': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Chicago%20Bears.csv',
        'Cincinnati Bengals': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Cincinnati%20Bengals.csv',
        'Cleveland Browns': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Cleveland%20Browns.csv',
        'Dallas Cowboys': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Dallas%20Cowboys.csv',
        'Denver Broncos': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Denver%20Broncos.csv',
        'Detroit Lions': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Detroit%20Lions.csv',
        'Green Bay Packers': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Green%20Bay%20Packers.csv',
        'Houston Texans': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Houston%20Texans.csv',
        'Indianapolis Colts': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Indianapolis%20Colts.csv',
        'Jacksonville Jaguars': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Jacksonville%20Jaguars.csv',
        'Kansas City Chiefs': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Kansas%20City%20Chiefs.csv',
        'Las Vegas Raiders': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Las%20Vegas%20Raiders.csv',
        'Los Angeles Chargers': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Los%20Angeles%20Chargers.csv',
        'Los Angeles Rams': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Los%20Angeles%20Rams.csv',
        'Miami Dolphins': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Miami%20Dolphins.csv',
        'Minnesota Vikings': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Minnesota%20Vikings.csv',
        'New England Patriots': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20New%20England%20Patriots.csv',
        'New Orleans Saints': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20New%20Orleans%20Saints.csv',
        'New York Giants': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20New%20York%20Giants.csv',
        'New York Jets': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20New%20York%20Jets.csv',
        'Philadelphia Eagles': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Philadelphia%20Eagles.csv',
        'Pittsburgh Steelers': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Pittsburgh%20Steelers.csv',
        'San Francisco 49ers': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20San%20Francisco%2049ers.csv',
        'Seattle Seahawks': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Seattle%20Seahawks.csv',
        'Tampa Bay Buccaneers': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Tampa%20Bay%20Buccaneers.csv',
        'Tennessee Titans': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Tennessee%20Titans.csv',
        'Washington Commanders': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Washington%20Commanders.csv',
}
        # Add other leagues and teams as necessary
    
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
}},
    # Assuming similar structure for NBA, NHL, MLB with their own URLs
}

def load_team_roster(league, team):
    """Load the team roster from a specified URL."""
    try:
        url = team_roster_urls[league][team]
        df = pd.read_csv(url)
        return df
    except KeyError:
        st.error(f"Roster URL for the selected team, {team}, in {league} is not available.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Failed to load the team roster: {e}")
        return pd.DataFrame()

# League selection
league_selection = st.sidebar.selectbox('Pick a League', ['Select a league'] + list(team_roster_urls.keys()))

if league_selection != 'Select a league':
    # Team selection based on the chosen league
    team_selection = st.sidebar.selectbox('Pick a Team', ['Select a team'] + list(team_roster_urls[league_selection].keys()))
    
    if team_selection != 'Select a team':
        # Load and display the roster for the selected team
        roster_df = load_team_roster(league_selection, team_selection)
        if not roster_df.empty:
            st.write(f"Roster for {team_selection}:")
            st.dataframe(roster_df)
    
    if not roster_df.empty:
        # UI to select a team within the selected league
        team = st.sidebar.selectbox('Select a Team', ['Select a team'] + sorted(roster_df['Team'].unique()))
        
        if team != 'Select a team':
            # Filter the DataFrame for the selected team
            team_df = roster_df[roster_df['Team'] == team]
            
            # Display the roster for the selected team
            st.write(f'Roster for {team}:')
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

