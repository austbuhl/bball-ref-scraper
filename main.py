import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple web scraping of NBA player stats!
* **Python Libraries:** base64, pandas, streamlit
* **Data Source:** [Basketball-reference.com](https://www.basketball-reference.com/)
""")