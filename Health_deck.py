import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.title('HealthAura: Pro Sports Tracker')

# Define a dictionary that maps each league to its corresponding team roster URLs
team_roster_urls = {
    'MLB': {team_name: f"https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20{team_name.replace(' ', '%20')}.csv" for team_name in [
         "San Francisco Giants", "Cleveland Guardians", "Seattle Mariners", "Miami Marlins", "New York Mets", "Washington Nationals", "Baltimore Orioles", "San Diego Padres", "Philadelphia Phillies", "Pittsburgh Pirates",
        "Texas Rangers", "Tampa Bay Rays", "Boston Red Sox", "Cincinnati Reds", "Colorado Rockies", "Kansas City Royals", "Detroit Tigers", "Minnesota Twins", "Chicago White Sox", "New York Yankees"
    ]},
    'NBA': {team_name: f"https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20{team_name.replace(' ', '%20')}.csv" for team_name in [
          "Philadelphia 76ers", "Milwaukee Bucks", "Chicago Bulls", "Cleveland Cavaliers", "Boston Celtics", "Los Angeles Clippers", "Memphis Grizzlies", "Atlanta Hawks", "Miami Heat", "Charlotte Hornets",
        "Utah Jazz", "Sacramento Kings", "New York Knicks", "Los Angeles Lakers", "Orlando Magic", "Dallas Mavericks", "Brooklyn Nets", "Denver Nuggets", "Indiana Pacers", "New Orleans Pelicans",
        "Detroit Pistons", "Toronto Raptors", "Houston Rockets", "San Antonio Spurs", "Phoenix Suns", "Oklahoma City Thunder", "Minnesota Timberwolves", "Portland Trail Blazers", "Golden State Warriors", "Washington Wizards"
    ]},
    'NFL': {team_name: f"https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20{team_name.replace(' ', '%20')}.csv" for team_name in [
         "San Francisco 49ers", "Chicago Bears", "Cincinnati Bengals", "Buffalo Bills", "Denver Broncos", "Cleveland Browns", "Tampa Bay Buccaneers", "Arizona Cardinals", "Los Angeles Chargers", "Kansas City Chiefs",
        "Indianapolis Colts", "Washington Commanders", "Dallas Cowboys", "Miami Dolphins", "Philadelphia Eagles", "Atlanta Falcons", "New York Giants", "Jacksonville Jaguars", "New York Jets", "Detroit Lions",
        "Green Bay Packers", "Carolina Panthers", "New England Patriots", "Las Vegas Raiders", "Los Angeles Rams", "Baltimore Ravens", "New Orleans Saints", "Seattle Seahawks", "Pittsburgh Steelers", "Houston Texans",
        "Tennessee Titans", "Minnesota Vikings"
    ]},
    'NHL': {team_name: f"https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20{team_name.replace(' ', '%20')}.csv" for team_name in [
         "Colorado Avalanche", "Chicago Blackhawks", "Columbus Blue Jackets", "St. Louis Blues", "Boston Bruins", "Montreal Canadiens", "Vancouver Canucks", "Washington Capitals", "Arizona Coyotes", "New Jersey Devils",
        "Anaheim Ducks", "Calgary Flames", "Philadelphia Flyers", "Vegas Golden Knights", "Carolina Hurricanes", "New York Islanders", "Winnipeg Jets", "Los Angeles Kings", "Seattle Kraken", "Tampa Bay Lightning",
        "Toronto Maple Leafs", "Edmonton Oilers", "Florida Panthers", "Pittsburgh Penguins", "Nashville Predators", "New York Rangers", "Detroit Red Wings", "Buffalo Sabres", "Ottawa Senators", "San Jose Sharks",
        "Dallas Stars", "Minnesota Wild"
    ]}
}

# Mapping NFL teams to their roster CSV URLs
mlb_team_roster_urls = {
    "Arizona Diamondbacks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Arizona%20Diamondbacks.csv",
    "Atlanta Braves": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Atlanta%20Braves.csv",
    "Baltimore Orioles": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Baltimore%20Orioles.csv",
    "Boston Red Sox": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Boston%20Red%20Sox.csv",
    "Chicago Cubs": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Chicago%20Cubs.csv",
    "Chicago White Sox": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Chicago%20White%20Sox.csv",
    "Cincinnati Reds": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Cincinnati%20Reds.csv",
    "Cleveland Guardians": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Cleveland%20Guardians.csv",
    "Colorado Rockies": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Colorado%20Rockies.csv",
    "Detroit Tigers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Detroit%20Tigers.csv",
    "Houston Astros": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Houston%20Astros.csv",
    "Kansas City Royals": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Kansas%20City%20Royals.csv",
    "Los Angeles Angels": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Los%20Angeles%20Angels.csv",
    "Los Angeles Dodgers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Los%20Angeles%20Dodgers.csv",
    "Miami Marlins": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Miami%20Marlins.csv",
    "Milwaukee Brewers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Milwaukee%20Brewers.csv",
    "Minnesota Twins": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Minnesota%20Twins.csv",
    "New York Mets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20New%20York%20Mets.csv",
    "New York Yankees": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20New%20York%20Yankees.csv",
    "Oakland Athletics": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Oakland%20Athletics.csv",
    "Philadelphia Phillies": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Philadelphia%20Phillies.csv",
    "Pittsburgh Pirates": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Pittsburgh%20Pirates.csv",
    "San Diego Padres": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20San%20Diego%20Padres.csv",
    "San Francisco Giants": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20San%20Francisco%20Giants.csv",
    "Seattle Mariners": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Seattle%20Mariners.csv",
    "St. Louis Cardinals": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20St.%20Louis%20Cardinals.csv",
    "Tampa Bay Rays": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Tampa%20Bay%20Rays.csv",
    "Texas Rangers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Texas%20Rangers.csv",
    "Toronto Blue Jays": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Toronto%20Blue%20Jays.csv",
    "Washington Nationals": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Washington%20Nationals.csv",
}
nba_team_roster_urls = {
    "Atlanta Hawks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Atlanta%20Hawks.csv",
    "Boston Celtics": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Boston%20Celtics.csv",
    "Brooklyn Nets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Brooklyn%20Nets.csv",
    "Charlotte Hornets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Charlotte%20Hornets.csv",
    "Chicago Bulls": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Chicago%20Bulls.csv",
    "Cleveland Cavaliers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Cleveland%20Cavaliers.csv",
    "Dallas Mavericks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Dallas%20Mavericks.csv",
    "Denver Nuggets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Denver%20Nuggets.csv",
    "Detroit Pistons": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Detroit%20Pistons.csv",
    "Golden State Warriors": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Golden%20State%20Warriors.csv",
    "Houston Rockets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Houston%20Rockets.csv",
    "Indiana Pacers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Indiana%20Pacers.csv",
    "Los Angeles Clippers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Los%20Angeles%20Clippers.csv",
    "Los Angeles Lakers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Los%20Angeles%20Lakers.csv",
    "Memphis Grizzlies": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Memphis%20Grizzlies.csv",
    "Miami Heat": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Miami%20Heat.csv",
    "Milwaukee Bucks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Milwaukee%20Bucks.csv",
    "Minnesota Timberwolves": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Minnesota%20Timberwolves.csv",
    "New Orleans Pelicans": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20New%20Orleans%20Pelicans.csv",
    "New York Knicks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20New%20York%20Knicks.csv",
    "Oklahoma City Thunder": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Oklahoma%20City%20Thunder.csv",
    "Orlando Magic": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Orlando%20Magic.csv",
    "Philadelphia 76ers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Philadelphia%2076ers.csv",
    "Phoenix Suns": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Phoenix%20Suns.csv",
    "Portland Trail Blazers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Portland%20Trail%20Blazers.csv",
    "Sacramento Kings": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Sacramento%20Kings.csv",
    "San Antonio Spurs": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20San%20Antonio%20Spurs.csv",
    "Toronto Raptors": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Toronto%20Raptors.csv",
    "Utah Jazz": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Utah%20Jazz.csv",
    "Washington Wizards": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Washington%20Wizards.csv"
}
nfl_team_roster_urls = {
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
nhl_team_roster_urls = {
    "Anaheim Ducks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Anaheim%20Ducks.csv",
    "Arizona Coyotes": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Arizona%20Coyotes.csv",
    "Boston Bruins": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Boston%20Bruins.csv",
    "Buffalo Sabres": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Buffalo%20Sabres.csv",
    "Calgary Flames": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Calgary%20Flames.csv",
    "Carolina Hurricanes": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Carolina%20Hurricanes.csv",
    "Chicago Blackhawks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Chicago%20Blackhawks.csv",
    "Colorado Avalanche": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Colorado%20Avalanche.csv",
    "Columbus Blue Jackets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Columbus%20Blue%20Jackets.csv",
    "Dallas Stars": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Dallas%20Stars.csv",
    "Detroit Red Wings": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Detroit%20Red%20Wings.csv",
    "Edmonton Oilers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Edmonton%20Oilers.csv",
    "Florida Panthers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Florida%20Panthers.csv",
    "Los Angeles Kings": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Los%20Angeles%20Kings.csv",
    "Minnesota Wild": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Minnesota%20Wild.csv",
    "Montreal Canadiens": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Montreal%20Canadiens.csv",
    "Nashville Predators": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Nashville%20Predators.csv",
    "New Jersey Devils": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20New%20Jersey%20Devils.csv",
    "New York Islanders": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20New%20York%20Islanders.csv",
    "New York Rangers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20New%20York%20Rangers.csv",
    "Ottawa Senators": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Ottawa%20Senators.csv",
    "Philadelphia Flyers": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Philadelphia%20Flyers.csv",
    "Pittsburgh Penguins": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Pittsburgh%20Penguins.csv",
    "San Jose Sharks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20San%20Jose%20Sharks.csv",
    "Seattle Kraken": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Seattle%20Kraken.csv",
    "St. Louis Blues": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20St.%20Louis%20Blues.csv",
    "Tampa Bay Lightning": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Tampa%20Bay%20Lightning.csv",
    "Toronto Maple Leafs": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Toronto%20Maple%20Leafs.csv",
    "Vancouver Canucks": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Vancouver%20Canucks.csv",
    "Vegas Golden Knights": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Vegas%20Golden%20Knights.csv",
    "Washington Capitals": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Washington%20Capitals.csv",
    "Winnipeg Jets": "https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Winnipeg%20Jets.csv",
}


# Function to load and display team roster with interactive dropdown integrated directly into the row
def display_team_roster(league, team, organize_by):
    url = team_roster_urls[league][team]
    try:
        # Load the CSV file
        roster_df = pd.read_csv(url)

        # Optionally, rename columns to ensure consistency
        column_mapping = {
            'Player': 'Player Name',  # Adjust as necessary
            'Team': 'Team Name',      # Adjust as necessary
        }
        roster_df.rename(columns=column_mapping, inplace=True)

        # Define columns to display in the main view
        main_columns = ['Team Name', 'Player Name', 'Career Health', 'Seasonal Health', 'Percent of Reinjury']
        details_columns = [col for col in roster_df.columns if col not in main_columns]

        # Sort the data if a valid sorting option is chosen
        if organize_by in roster_df.columns and organize_by != 'Default':
            sort_ascending = False  # Set to True if ascending order is preferred
            roster_df = roster_df.sort_values(by=organize_by, ascending=sort_ascending)

        # Display the team roster
        st.write(f"Roster for {team}:")
        for index, row in roster_df.iterrows():
            cols = st.columns(5)  # Create columns for each of the main data points
            cols[0].write(row['Team Name'])
            with cols[1].expander(f"{row['Player Name']}"):
                st.write("Additional details about the player.")
            with cols[2].expander(f"{row['Career Health']}"):
                st.write("Details about past injuries will appear here.")
            with cols[3].expander(f"{row['Seasonal Health']}"):
                st.write("Details about current season injuries will appear here.")
            cols[4].write(row['Percent of Reinjury'])

    except Exception as e:
        st.error(f"Failed to load roster: {e}")

# Streamlit app interface
league_choice = st.sidebar.selectbox('Select a League', ['Select a League'] + list(team_roster_urls.keys()))
if league_choice != 'Select a League':
    teams_list = list(team_roster_urls[league_choice].keys())
    team_choice = st.sidebar.selectbox('Select a Team', ['Select a Team'] + sorted(teams_list))

    organize_options = {
        'MLB': ["Default", "Team Name", "Player Number", "Position", "DOB", "Career Health", "Seasonal Health", "Percent of Reinjury", "Status", "Base Salary"],
        'NBA': ["Default", "Player Name", "Career Health", "Seasonal Health", "Percent of Reinjury"],
        'NFL': ["Default", "Player Name", "Career Health", "Seasonal Health", "Percent of Reinjury"],
        'NHL': ["Default", "Player Name", "Career Health", "Season Health", "Percent of Reinjury"]
    }
    if league_choice in organize_options:
        organize_by = st.sidebar.selectbox('Organize Data', organize_options[league_choice])
    else:
        organize_by = 'Default'
    
    if team_choice != 'Select a Team':
        display_team_roster(league_choice, team_choice, organize_by)
