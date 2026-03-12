import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Krankenkassen CX Benchmark")

df = pd.read_csv("cx_benchmark_dataset.csv")

st.subheader("Benchmark Tabelle")
st.dataframe(df)

st.subheader("CX Score Ranking")
fig = px.bar(df.sort_values("cx_gesamt_score",ascending=False),
             x="krankenkasse_name",
             y="cx_gesamt_score")

st.plotly_chart(fig)

kasse = st.selectbox("Krankenkasse auswählen", df["krankenkasse_name"])

details = df[df["krankenkasse_name"]==kasse]

st.subheader("KPIs")

st.write(details)

rec = pd.read_csv("recommendations.csv")

st.subheader("Handlungsempfehlungen")

st.write(rec[rec["krankenkasse"]==kasse])
