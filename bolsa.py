import yfinance
import streamlit as st

st.set_page_config(
    page_title="Dashboard Ações",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon=":moneybag:",
)

st.title("Dashboard de Ações")

st.header("Fechamento e Dividendo de Ações")

ticker = st.text_input("Digite o ticker da ação:", "WEGE3")
empresa = yfinance.Ticker(f"{ticker}.SA")
tickerDF = empresa.history(period="5y", start="2020-01-01", end=None)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("Empresa:", empresa.info["longName"])
with col2:
    st.write("Mercado:", empresa.info["industry"])
with col3:
    st.write("Preço Atual:", empresa.info["currentPrice"], "BRL")

st.write("Fechamento e Dividendo de Ações")

st.line_chart(tickerDF["Close"])
st.line_chart(tickerDF["Dividends"])
