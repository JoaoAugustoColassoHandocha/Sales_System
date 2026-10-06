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

st.set_page_config(page_title = 'Sistema de Vendas', page_icon = '.\\vendas.ico')

sales_table = pd.read_csv('.\\vendas.csv')

write('# Sistema de Vendas')

st.sidebar.write('## Cadastrar Vendas')
date = st.sidebar.date_input('Data', max_value = 'today')
salesperson = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
product = st.sidebar.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantity = st.sidebar.number_input('Quantidade', step = 1)
amount = st.sidebar.number_input('Valor')
register_button = st.sidebar.button('Cadastrar Venda')

if register_button:
    
    if quantity <= 0 or amount <= 0:
        
        st.warning('Informações incorretas!!!')
    
    else:
        
        new_sale = [str(date), salesperson, product, quantity, amount]
        last_line = len(sales_table)
        sales_table.loc[last_line] = new_sale
        sales_table.to_csv('.\\vendas.csv', index = False)
        st.success('Venda cadastrada!')

write('## Vendas Cadastradas')
st.dataframe(sales_table)

write('## Dashboard')

invoicing = sales_table['valor'].sum()
st.metric('Faturamento Total', f'R$ {invoicing:.2f}')

bar_chart = px.bar(sales_table, x = 'vendedor', y = 'valor', color = 'produto')
st.plotly_chart(bar_chart)

pie_chart = px.pie(sales_table, names = 'produto', values = 'valor', hole = 0.5)
st.plotly_chart(pie_chart)