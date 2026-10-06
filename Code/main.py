'''
Update main.py

1 - Create the system screen
2 - Create the registration form
3 - Save the sale to the database
4 - Display the database on the screen
5 - Create the dashboard with charts

pip install streamlit pandas plotly - Imported libraries

streamlit run main.py - Runs the application

'''

import streamlit as st
import pandas as pd
import plotly.express as px

write = st.write
title = st.title

title('# Sistema de Vendas')

write('# Sistema de Vendas')

write('## Cadastrar Vendas')

write('## Vendas Cadastradas')

write('## Dashboard')