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

st.set_page_config(page_title = 'Sistema de Vendas', page_icon = 'vendas.ico')

write('# Sistema de Vendas')

write('## Cadastrar Vendas')

date = st.date_input('Data')
salesperson = st.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
product = st.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantity = st.number_input('Quantidade')
amount = st.number_input('Valor')
register_button = st.button('Cadastrar Venda')

write('## Vendas Cadastradas')

write('## Dashboard')