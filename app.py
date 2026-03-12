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
