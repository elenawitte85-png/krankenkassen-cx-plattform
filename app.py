import streamlit as st
import pandas as pd

st.set_page_config(page_title="Krankenkassen CX Plattform", layout="wide")
st.title("Krankenkassen CX Analyse")

# Daten laden
df = pd.read_csv("data.csv")

# Datenübersicht
st.subheader("Datenübersicht")
st.dataframe(df)

# Ranking Gesamt-Score
st.subheader("Ranking Gesamt-Score")
st.table(df.sort_values("Gesamt_Score", ascending=False)[["Krankenkasse", "Gesamt_Score"]])

# Ranking Kundenzufriedenheit
st.subheader("Ranking Kundenzufriedenheit")
st.table(df.sort_values("Kunden_Zufriedenheit", ascending=False)[["Krankenkasse", "Kunden_Zufriedenheit"]])

# Ranking Reputation
st.subheader("Ranking Reputation")
st.table(df.sort_values("Reputation", ascending=False)[["Krankenkasse", "Reputation"]])

# SWOT Analyse
st.subheader("SWOT Analyse")
kasse = st.selectbox("Krankenkasse wählen", df["Krankenkasse"])
kasse_data = df[df["Krankenkasse"] == kasse].iloc[0]

st.markdown(f"""
**Strength:** Hohe Gesamtbewertung ({kasse_data['Gesamt_Score']})  
**Weakness:** Zusatzbeitrag ({kasse_data['Zusatzbeitrag']})  
**Opportunity:** Verbesserung der Kundenzufriedenheit ({kasse_data['Kunden_Zufriedenheit']})  
**Threat:** Online-Reputation ({kasse_data['Reputation']})  
**Digital App:** {kasse_data['App_Award']}
""")
