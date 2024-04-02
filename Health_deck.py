
import streamlit as st
import pandas as pd
import numpy as np

st.title('HealthAura: Pro Sports Tracker')

# Define options for the selectbox with sports leagues
sports_options = ['NFL', 'NBA', 'NHL', 'MLB']

# Add a selectbox to the sidebar with a title
sport_choice = st.sidebar.selectbox('Sports', sports_options)

# Display the selected sport
st.write(f'You selected: {sport_choice}')

# Conditional content based on sport choice
if sport_choice == 'NFL':
    st.write('Displaying NFL data...')
    # Add your code here to display NFL specific data or analysis
elif sport_choice == 'NBA':
    st.write('Displaying NBA data...')
    # Add your code here to display NBA specific data or analysis
elif sport_choice == 'NHL':
    st.write('Displaying NHL data...')
    # Add your code here to display NHL specific data or analysis
elif sport_choice == 'MLB':
    st.write('Displaying MLB data...')
    # Add your code here to display MLB specific data or analysis

# Sample DataFrame creation for demonstration
# In real-life applications, load this data from a more dynamic source like a database or API
data = {
    'Name': ['Player 1', 'Player 2', 'Player 3'],
    'Position': ['Position A', 'Position B', 'Position C'],
    'Seasonal Health': [90, 80, 85],
    'Career Health': [95, 89, 92],
    'Percent of Reinjury': [5, 10, 15],
    'Injury Date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01']),
    'Agent': ['Agent X', 'Agent Y', 'Agent Z']
}
df = pd.DataFrame(data)

st.title('HealthAura: Pro Sports Tracker')

# Sidebar for sport selection
sports_options = ['Select a sport', 'NFL', 'NBA', 'NHL', 'MLB']
sport_choice = st.sidebar.selectbox('Sports', sports_options)

# Conditional sidebar for organizing data based on sport choice
if sport_choice != 'Select a sport':
    # Define generic organization options, you can customize this per sport as needed
    organization_options = {
        'NFL': ['Alphabetical', 'By Position', 'By Seasonal Health', 'By Career Health', 'By Percent of Reinjury', 'By Injury Date', 'By Agent'],
        'NBA': ['Alphabetical', 'By Position', 'By Seasonal Health', 'By Career Health', 'By Percent of Reinjury', 'By Injury Date', 'By Agent'],
        'NHL': ['Alphabetical', 'By Position', 'By Seasonal Health', 'By Career Health', 'By Percent of Reinjury', 'By Injury Date', 'By Agent'],
        'MLB': ['Alphabetical', 'By Position', 'By Seasonal Health', 'By Career Health', 'By Percent of Reinjury', 'By Injury Date', 'By Agent']
    }

    # Update organization choice based on sport
    organization_choice = st.sidebar.selectbox('Organize Data By', organization_options[sport_choice])

    # Organizing data based on the choice
    if organization_choice == 'Alphabetical':
        sorted_df = df.sort_values(by='Name')
    elif organization_choice == 'By Position':
        sorted_df = df.sort_values(by='Position')
    elif organization_choice == 'By Seasonal Health':
        sorted_df = df.sort_values(by='Seasonal Health', ascending=False)
    elif organization_choice == 'By Career Health':
        sorted_df = df.sort_values(by='Career Health', ascending=False)
    elif organization_choice == 'By Percent of Reinjury':
        sorted_df = df.sort_values(by='Percent of Reinjury', ascending=False)
    elif organization_choice == 'By Injury Date':
        sorted_df = df.sort_values(by='Injury Date')
    elif organization_choice == 'By Agent':
        sorted_df = df.sort_values(by='Agent')

    # Display the sorted DataFrame
    st.write(f'You selected: {sport_choice}')
    st.write('Data organized by:', organization_choice)
    st.dataframe(sorted_df)
else:
    st.write("Please select a sport to view and organize data.")
