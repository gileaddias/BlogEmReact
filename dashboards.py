import streamlit as streamlit
import pandas as pd
import plotly.express as px

st.set_page_config(layout+"wide")

# Com uma visão mensal
#faturamento por unidade_ 
#tipo de produto mais vendido, contribuição por filial,
#Desenpenho das formas de pagamento_
#Como estão as avaliações das filiais?
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
