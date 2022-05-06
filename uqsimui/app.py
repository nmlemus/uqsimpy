import streamlit as st

from gui.sidebar import *
from gui.create_model import *

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

objective = set_sidebar(st)

if objective == 'Create Model':
    CreateModel(st)
elif objective == 'Info':
    CreateModel(st) 
