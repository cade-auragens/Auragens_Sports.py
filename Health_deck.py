
import streamlit as st
import pandas as pd
import numpy as np

st.title('HealthAura: Pro Sports Tracker')

from streamlit_option_menu import option_menu

with st.sidebar:
  menu_title= "Sports"
  options = ["NFL", "NBA", "MLB"],
