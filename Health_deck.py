
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

df = pd.DataFrame(data)

st.title('HealthAura: Pro Sports Tracker')

# Step 1: Select a Team
team_choice = st.sidebar.selectbox('Select a Team', df['Team Name'].unique())

# Step 2: Display Team Roster
if team_choice:
    team_df = df[df['Team Name'] == team_choice]
    # Display basic team roster information
    for _, row in team_df.iterrows():
        st.text(f"{row['Player Name']} - Career Health: {row['Career Health']}%, Seasonal Health: {row['Seasonal Health']}%, Injury Risk: {row['Percent of Injury']}%")
    
    # Step 3: Select a Player to view more details
    player_choice = st.sidebar.selectbox('Select a Player', team_df['Player Name'].unique())
    
    if player_choice:
        player_df = team_df[team_df['Player Name'] == player_choice].iloc[0]
        
        # Display detailed player information
        st.subheader(f"Details for {player_choice}")
        st.text(f"Position: {player_df['Position']}")
        st.text(f"Height: {player_df['Height']}")
        st.text(f"Weight: {player_df['Weight']}")
        st.text(f"Age: {player_df['Age']}")
        st.text(f"Years of Experience: {player_df['Years of Experience']}")
        st.text(f"Agent: {player_df['Agent']} ({player_df['Agent Email']}, {player_df['Agency']})")
        
        # Display player's injury history
        # Assuming you have a method to fetch injury history for the player
        injury_history = get_injury_history(player_choice)  # Placeholder for actual injury history retrieval function
        st.text("Injury History:")
        for injury in injury_history:
            st.text(injury)


