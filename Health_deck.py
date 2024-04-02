
import streamlit as st
import pandas as pd
import numpy as np

# Path to the logo image (assuming it's in the same directory as your script)
logo_path = ''

# Display the logo at the top using st.image
st.image(logo_path, width=100)  # Adjust the width as needed

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
