import streamlit as st
import pandas as pd

st.title("Krankenkassen CX Vergleich")

data = {
"Krankenkasse": [
"Techniker Krankenkasse",
"AOK",
"Barmer",
"DAK-Gesundheit"
],
"App Rating":[4.6,3.8,4.2,3.9],
"NPS":[45,30,38,33],
"Bearbeitungszeit":[3,5,4,4.5]
}

df = pd.DataFrame(data)

st.subheader("Datenübersicht")
st.dataframe(df)

st.subheader("Ranking Digitalisierung")
st.table(df.sort_values("App Rating", ascending=False)[["Krankenkasse","App Rating"]])

st.subheader("Ranking Service Geschwindigkeit")
st.table(df.sort_values("Bearbeitungszeit")[["Krankenkasse","Bearbeitungszeit"]])
