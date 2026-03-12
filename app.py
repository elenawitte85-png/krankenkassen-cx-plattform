import streamlit as st
import pandas as pd

st.set_page_config(page_title="Krankenkassen CX Plattform – erweitert", layout="wide")
st.title("Krankenkassen CX Analyse – Praxisnahe KPIs")

# Daten laden
df = pd.read_csv("data.csv")

# Tabellenübersicht
st.subheader("Alle Krankenkassen und KPIs")
st.dataframe(df)

# Rankings nach KPIs
st.subheader("Ranking nach Gesamt_Score")
st.table(df.sort_values("Gesamt_Score", ascending=False)[["Krankenkasse","Gesamt_Score","Digital_Score"]])

st.subheader("Ranking nach Service_Index")
st.table(df.sort_values("Service_Index", ascending=False)[["Krankenkasse","Service_Index"]])

st.subheader("Ranking nach Reputation_Score")
st.table(df.sort_values("Reputation_Score", ascending=False)[["Krankenkasse","Reputation_Score"]])

st.subheader("Ranking nach Social_Media_Sentiment")
st.table(df.sort_values("Social_Media_Sentiment", ascending=False)[["Krankenkasse","Social_Media_Sentiment"]])

st.subheader("SWOT-Analyse")
kasse = st.selectbox("Krankenkasse wählen", df["Krankenkasse"])
d = df[df["Krankenkasse"]==kasse].iloc[0]

st.markdown(f"""
**Strength:** Gesamt-Score {d['Gesamt_Score']} und Digital-Score {d['Digital_Score']}  
**Weakness:** Zusatzbeitrag {d['Zusatzbeitrag']}%  
**Opportunity:** Service_Index {d['Service_Index']} & Bonus_Index {d['Bonus_Index']}  
**Threat:** Reputation_Score {d['Reputation_Score']} & Social_Media_Sentiment {d['Social_Media_Sentiment']}  
**Präventionsprogramme:** {d['Praeventions_Index']} (Index)  
""")
