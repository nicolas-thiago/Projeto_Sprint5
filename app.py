import pandas as pd
import plotly.express as px
import streamlit as st

# Título do app
st.title('Análise de Veículos Usados')

# Carregamento dos dados
car_data = pd.read_csv('vehicles_us.csv')

# Botão para mostrar histograma do odômetro
if st.button('Mostrar histograma do odômetro'):
    st.write('Distribuição dos valores de odômetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para mostrar gráfico de dispersão odômetro vs preço
if st.checkbox('Mostrar dispersão: Odômetro x Preço'):
    st.write('Relação entre odômetro e preço')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
