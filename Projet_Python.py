import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import yfinance as yf
from librairie.lib import indic_tec



######################################### titre: Cour de bourse de l'action Tesla


#st.title('Le cour de bourse de Tesla') 
st.markdown('Projet python')
st.sidebar.title('Selecteur de visualisation')

###Fonction get_data 
#@st.cache(persist=True) 
def data_finance(symbol):
    donnee = yf.Ticker(symbol)
    produit = donnee.history(period='max')
    produit = produit.drop(['Dividends','Stock Splits'], axis=1)
    return produit

actions = ['TSLA','HSBC','MRO']
actif = []
for action in actions:
    donnee = data_finance(f'{action}')
    donnee.reset_index(inplace=True)
    donnee = donnee.sort_values("Date", ascending = False)
    # Ajout de l'indicateur technique
    data_indic_tec = indic_tec(donnee)
    actif.append(data_indic_tec)
#st.write(actif[1])
st.markdown("""---""")

### titre : Action HSBC
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Action cour: ")
    st.subheader("HSBC")
with right_column:
    st.subheader("Prix moyen par transaction: {}".format(round(actif[1].iloc[0]['Close'])))

if st.checkbox("Voir les données journalières de HSBC"):
    st.write(actif[1])

st.title("COUR DE L'ACTION HSBC")
HSBC_COUR = actif[1]['Close']
chart_HSBC_COUR = HSBC_COUR.iloc[:300]
st.line_chart(chart_HSBC_COUR)

if st.checkbox("Voir RSI (indicateur technique / HSBC)"):
    st.title("EVOLUTION DES DONNÉES PAR RAPPORT AU RSI")
    HSBC_RSI = actif[1]['RSI']
    chart_HSBC_RSI = HSBC_RSI.iloc[:500]
    st.line_chart(chart_HSBC_RSI)

# Moyenne mobile
if st.checkbox("Voir MM (moyenne mobile / HSBC)"):
    st.title("EVOLUTION DES DONNÉES PAR RAPPORT A LA MOYENNE MOBILE")
    HSBC_RSI = actif[1]['MACD']
    chart_HSBC_RSI = HSBC_RSI.iloc[:500]
    st.line_chart(chart_HSBC_RSI)

    
################################################### Action TSLA
st.markdown("""---""")

### titre : Action TSLA
left_column1, middle_column1, right_column1 = st.columns(3)
with left_column1:
    st.subheader("Action cour: ")
    st.subheader("TSLA")
with right_column1:
    st.subheader("Prix moyen par transaction: {}".format(round(actif[0].iloc[0]['Close'])))

if st.checkbox("Voir les données journalières de TESLA"):
    st.write(actif[0])

st.title("COUR DE L'ACTION TESLA")
TSLA_COUR = actif[1]['Close']
chart_TSLA_COUR = TSLA_COUR.iloc[:300]
st.line_chart(chart_TSLA_COUR)

if st.checkbox("Voir RSI (indicateur technique / Tesla)"):
    st.title("EVOLUTION DES DONNÉES PAR RAPPORT AU RSI")
    TSLA_RSI = actif[0]['RSI']
    chart_TSLA_RSI = TSLA_RSI.iloc[:500]
    st.line_chart(chart_TSLA_RSI)

# Moyenne mobile
if st.checkbox("Voir MM (moyenne mobile) / TESLA"):
    st.title("EVOLUTION DES DONNÉES PAR RAPPORT A LA MOYENNE MOBILE")
    TSLA_RSI = actif[0]['MACD']
    chart_TSLA_RSI = TSLA_RSI.iloc[:500]
    st.line_chart(chart_TSLA_RSI)

############################## END

##################################### Action MRO

st.markdown("""---""")

### titre : Action TSLA
left_column1, middle_column1, right_column1 = st.columns(3)
with left_column1:
    st.subheader("Action cour: ")
    st.subheader("MARATHON OIL CORP.")
with right_column1:
    st.subheader("Prix moyen par transaction: {}".format(round(actif[2].iloc[0]['Close'])))

if st.checkbox("Voir les données journalières de Marathon Oil"):
    st.write(actif[2])

st.title("COUR DE L'ACTION MARATHON OIL")
MRO_COUR = actif[2]['Close']
chart_MRO_COUR = MRO_COUR.iloc[:300]
st.line_chart(chart_MRO_COUR)

if st.checkbox("Voir RSI (indicateur technique / Marathon Oil)"):
    st.title("EVOLUTION DES DONNÉES PAR RAPPORT AU RSI")
    MRO_RSI = actif[2]['RSI']
    chart_MRO_RSI = MRO_RSI.iloc[:500]
    st.line_chart(chart_MRO_RSI)

# Moyenne mobile
if st.checkbox("Voir MM (moyenne mobile) / Marathon Oil"):
    st.title("EVOLUTION DES DONNÉES PAR RAPPORT A LA MOYENNE MOBILE")
    MRO_RSI = actif[2]['MACD']
    chart_MRO_RSI = MRO_RSI.iloc[:500]
    st.line_chart(chart_MRO_RSI)
################################ END


