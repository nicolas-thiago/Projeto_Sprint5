import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análise de Carros Usados')

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="Odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')
    fig2 = px.scatter(car_data, x='Odometer', y='Price')
    st.plotly_chart(fig2, use_container_width=True)