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

sales_table = pd.read_csv('vendas.csv')

write('# Sistema de Vendas')

write('## Cadastrar Vendas')

date = st.date_input('Data')
salesperson = st.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
product = st.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantity = st.number_input('Quantidade', step = 1)
amount = st.number_input('Valor')
register_button = st.button('Cadastrar Venda')

write('## Vendas Cadastradas')

st.dataframe(sales_table)

write('## Dashboard')

invoicing = sales_table['valor'].sum()

st.metric('Faturamento Total', f'R$ {invoicing:.2f}')

bar_chart = px.bar(sales_table, x = 'vendedor', y = 'valor', color = 'produto')

pie_chart = px.pie()