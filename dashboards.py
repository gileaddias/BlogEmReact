import streamlit as streamlit
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal
#faturamento por unidade_ 
#tipo de produto mais vendido, contribuição por filial,
#Desenpenho das formas de pagamento_
#Como estão as avaliações das filiais?
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")


df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("M~es", df["Month"].unique())

df_filtered =  df[df["Month"] == month]

col1, col2 = st.colums(2)
col3, col4, col5 = st.colums(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City" title="Faturamento por Dia")
col1.plotly_chart(fig_date. use_container_width=true)

prod_date = px.bar(df_filtered, x="Date", y="Product line",
                 color="City" title="Faturamento por tipo de Produto",
                 orientation="h")
col2.plotly_chart(fig_prod. use_container_width=true)


city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index
fig_city = px.bar(city_total, x="City", y="Total",
                title="Faturamento por Filial")
col3.plotly_chart(fig_city. use_container_width=true)


fig_city = px.pie(df_filtered, values="Total", names="Payment",
                title="Faturamento por Tipo de Pagamento")
col4.plotly_chart(fig_kind. use_container_width=true)


city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City",
                title="Avaliação")
col5.plotly_chart(fig_rating. use_container_width=true)