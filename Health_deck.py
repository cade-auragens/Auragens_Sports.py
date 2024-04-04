
import streamlit as st
import pandas as pd

st.title('HealthAura: Pro Sports Tracker')

# Provided dictionary for teams by sport
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

# Mapping of leagues to their respective GitHub raw CSV file URLs
roster_urls = {
    'NFL': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NFL%20Roster.csv',
    'NBA': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NBA%20Roster.csv',
    'NHL': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/NHL%20Roster.csv',
    'MLB': 'https://raw.githubusercontent.com/cade-auragens/Auragens_Sports.py/main/MLB%20Roster.csv',
}

def load_roster_data(league, team):
    """Load roster data from a GitHub-hosted CSV file for a selected team."""
    url = roster_urls.get(league)
    if url:
        df = pd.read_csv(url)
        return df[df['Team'] == team]
    else:
        st.error(f"No data found for the league: {league}")
        return pd.DataFrame()

# League selection
league_selection = st.sidebar.selectbox('Pick a League', ['Select a league'] + list(teams_by_sport.keys()))

if league_selection != 'Select a league':
    # Team selection based on the chosen league
    team_selection = st.sidebar.selectbox('Pick a Team', ['Select a team'] + teams_by_sport[league_selection])
    
    if team_selection != 'Select a team':
        # Load and display the roster for the selected team
        team_df = load_roster_data(league_selection, team_selection)
        
        # Display options to organize the roster data
        organization_options = [
            'Select organization',
            'Alphabetical',
            'By Position',
            'By Seasonal Health',
            'By Career Health',
            'By Percent of Reinjury',
            'By Injury Date',
            'By Agent'
        ]
        organization_choice = st.sidebar.selectbox('Organize Data By', organization_options)
        
        # Apply organization choice to the DataFrame
        if organization_choice != 'Select organization':
            if organization_choice == 'Alphabetical':
                team_df = team_df.sort_values(by='Name')
            elif organization_choice == 'By Position':
                team_df = team_df.sort_values(by='Position')
            # Additional sorting options here...

        st.write(f"Roster for {team_selection}:")
        st.dataframe(team_df[['Name', 'Pos', 'Ht', 'WT', 'Age', 'Yrs of EXP']], width=800)

