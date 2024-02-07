pip install yfinance
import yfinance as yf
import streamlit as st

st.title("Preço do ativo")
st.header("Informações a respeito do fechamento de ações")

opcoes = st.selectbox('Escolha o ativo',('BBAS3.SA','BBDC4.SA','PETR4.SA','VALE5.SA'))

tickerSimbolo = opcoes
tickerData = yf.Ticker(tickerSimbolo)

tickerDF = tickerData.history(period = "1d",start="2012-5-19",end="2022-5-19")
print(tickerDF)
st.header("Grafico de Fechamento")
st.line_chart(tickerDF.Close)

st.header("Grafico de volume")
st.line_chart(tickerDF.Volume)

st.header("Grafico de dividendos")
st.line_chart(tickerDF.Dividends)

