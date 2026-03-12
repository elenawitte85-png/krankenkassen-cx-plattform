import streamlit as st
import pandas as pd

st.set_page_config(page_title="Krankenkassen CX Plattform", layout="wide")
st.title("Krankenkassen CX Analyse – Praxisnahe KPIs & Empfehlungen")

# Daten laden
df = pd.read_csv("data.csv")

# Empfehlungen (Beispiel Mobil Krankenkasse)
recommendations = {
    "Mobil Krankenkasse": [
        {"Maßnahme": "Service-Schulungen für Kundenservice-Mitarbeiter",
         "Begründung": "Service_Index 67.5 liegt deutlich unter Top-Kassen (~75-77), Bearbeitungszeit und Freundlichkeit verbessern."},
        {"Maßnahme": "Einführung Ticket-Tracking & SLA-System",
         "Begründung": "Service_Index niedrig → Bearbeitungszeiten messen und standardisieren."},
        {"Maßnahme": "Social-Media-Monitoring und aktive Reaktion",
         "Begründung": "Social_Media_Sentiment nur 56% → Beschwerden schneller beantworten, positives Feedback sichtbar machen."},
        {"Maßnahme": "App-Optimierung und neue digitale Features",
         "Begründung": "Digital_Score 7.6/10 → Features wie Upload von Dokumenten, Chat, Online-Termine steigern UX."},
        {"Maßnahme": "Bonus- und Präventionsprogramme ausbauen",
         "Begründung": "Bonus_Index und Präventions_Index nur 5/10 → Maßnahmen wie Fitnesskurse, Gamification, Kooperationen erhöhen Kundenzufriedenheit."},
        {"Maßnahme": "Preisvorteil klar kommunizieren",
         "Begründung": "Zusatzbeitrag 2.75% unter Branchendurchschnitt → Vorteil als Marketing nutzen."},
        {"Maßnahme": "Trend_12M regelmäßig überwachen",
         "Begründung": "Trend_12M=0 → Fortschritt messen, Maßnahmen priorisieren (Impact/Aufwand)."}
    ]
}

# Tabellenansicht
st.subheader("Alle Krankenkassen und KPIs")
st.dataframe(df)

# Kasse auswählen
st.subheader("SWOT & Handlungsempfehlungen")
kasse = st.selectbox("Krankenkasse wählen", df["Krankenkasse"])

# SWOT
d = df[df["Krankenkasse"]==kasse].iloc[0]
st.markdown(f"""
**Strength:** Gesamt-Score {d['Gesamt_Score']} und Digital-Score {d['Digital_Score']}  
**Weakness:** Zusatzbeitrag {d['Zusatzbeitrag']}%, Service_Index {d['Service_Index']}  
**Opportunity:** Bonus_Index {d['Bonus_Index']}, Präventions_Index {d['Praeventions_Index']}  
**Threat:** Reputation_Score {d['Reputation_Score']}, Social_Media_Sentiment {d['Social_Media_Sentiment']}  
""")

# Handlungsempfehlungen
st.markdown("### Konkrete Handlungsempfehlungen & Begründung")
if kasse in recommendations:
    for rec in recommendations[kasse]:
        st.markdown(f"- **Maßnahme:** {rec['Maßnahme']}\n  - **Warum:** {rec['Begründung']}")
else:
    st.info("Keine spezifischen Empfehlungen verfügbar für diese Kasse.")
