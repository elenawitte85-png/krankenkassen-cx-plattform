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
st.dataframe(df)

# Oder Detailinfos als Sidebar-Tooltip
st.sidebar.subheader("KPI Erklärungen")
st.sidebar.markdown("""
**Gesamt_Score:** Gesamtbewertung 0–100 aus Service, Digital, Zusatzleistungen  
**Service_Index:** Bewertung Kundendienst (Bearbeitung, Freundlichkeit, Erreichbarkeit)  
**Reputation_Score:** Online-Reputation aus Social Media und Portalen  
**Social_Media_Sentiment:** % positive Erwähnungen online  
**Zusatzbeitrag:** Beitragssatz 2026 (%)  
**Digital_Score:** Bewertung digitaler Services / Apps  
**Trend_12M:** Veränderung Gesamt_Score ggü. Vorjahr  
**Bonus_Index:** Bonus-/Präventionsangebote (0–10)  
**Praeventions_Index:** Qualität der Präventionsprogramme (0–10)
""")
st.dataframe(df, tooltip={
    "Gesamt_Score": "Gesamtbewertung 0–100. Quelle: health-insurance.de, DISQ. Scoring: 40% Service, 30% Bonus/Prävention, 30% Digital",
    "Service_Index": "Kundenservice 0–100. Quelle: DISQ ServiceValue. Scoring: Mittelwert aus Umfragen",
    "Reputation_Score": "Online-Reputation 0–100. Quelle: Bewertungsportale, Social Media. Scoring: aggregiertes Sentiment",
    "Social_Media_Sentiment": "Anteil positiver Erwähnungen (%). Quelle: Social Media Monitoring",
    "Zusatzbeitrag": "Beitrag 2026 (%). Quelle: Kassen-Websites, Zusatzbeitrag.net",
    "Digital_Score": "0–10 Punkte. Quelle: App Store, Focus Money Siegel",
    "Trend_12M": "Veränderung Gesamt_Score ggü. Vorjahr",
    "Bonus_Index": "0–10 Punkte. Quelle: Kassen-Websites, Siegel",
    "Praeventions_Index": "0–10 Punkte. Quelle: Kassen-Websites, Siegel"
})
st.sidebar.subheader("KPI-Erklärungen")
st.sidebar.markdown("""
**Gesamt_Score:** Gesamtbewertung 0–100, aggregiert aus Service, Bonus/Prävention, Digital  
**Service_Index:** 0–100, Kundenzufriedenheit (DISQ/ServiceValue)  
**Reputation_Score:** 0–100, Online-Reputation (Social Media, Bewertungsportale)  
**Social_Media_Sentiment:** % positiver Erwähnungen in Social Media  
**Zusatzbeitrag:** Beitragssatz 2026 (%)  
**Digital_Score:** 0–10, Bewertung der Apps & digitalen Services  
**Trend_12M:** Veränderung Gesamt_Score ggü. Vorjahr  
**Bonus_Index:** 0–10, Qualität/Anzahl von Bonusprogrammen  
**Praeventions_Index:** 0–10, Qualität/Anzahl Präventionsmaßnahmen
""")
