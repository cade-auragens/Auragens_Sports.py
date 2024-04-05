import streamlit as st
import pandas as pd

st.title('HealthAura: Pro Sports Tracker')

# Mapping NFL teams to their roster CSV URLs
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

# Simplified to focus on the NFL; extend this to other leagues as needed
team_roster_urls = {'NFL': nfl_team_roster_urls}

def load_team_roster(team_url):
    """Load and return the team roster from a CSV URL."""
    try:
        df = pd.read_csv(team_url)
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()

# League selection (NFL only for this example)
league_selection = 'NFL'  # Hardcoded for simplification; use a selectbox for multiple leagues

if league_selection:
    # Team selection based on the chosen league (NFL)
    team_selection = st.sidebar.selectbox('Select a Team', ['Select a team'] + list(team_roster_urls[league_selection].keys()))
    
    if team_selection != 'Select a team':
        # Load and display the selected team's roster
        team_url = team_roster_urls[league_selection][team_selection]
        roster_df = load_team_roster(team_url)
        
        if not roster_df.empty:
            st.write(f"Roster for {team_selection}:")
            st.dataframe(roster_df)
