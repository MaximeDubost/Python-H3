import streamlit as st
import pandas as pd

st.write("##### Maxime DUBOST")
st.write("##### M1 IoT")
st.write("##### 17/11/2020")

st.title("TP : réalisation d'une data app ")
st.write("Votre mission est de construire une petite application de visualisation interactive de données avec l’outil Streamlit vu au chapitre précédent, qui contiendra les fonctionnalités suivantes :")

# ----------------------------------------------------------------

st.write("## - Charger des jeux de données (au moins 2) présents dans votre répertoire local")

st.write("**Dataset 1 :** Localisations des pays")
st.write("**Dataset 2 :** Localisations des états des USA")
st.write("Lien vers le dataset (2 en 1) : *https://www.kaggle.com/paultimothymooney/latitude-and-longitude-for-every-country-and-state/version/1*")

df1 = pd.read_csv('C:/Users/Maxime/Python/TP_Streamlit/world_country_and_usa_states_latitude_and_longitude_values.csv')[['country_code', 'latitude', 'longitude', 'country']].dropna()
df2 = pd.read_csv('C:/Users/Maxime/Python/TP_Streamlit/world_country_and_usa_states_latitude_and_longitude_values.csv')[['usa_state_code', 'usa_state_latitude', 'usa_state_longitude', 'usa_state']].rename(columns={'usa_state_latitude': 'latitude', 'usa_state_longitude': 'longitude'}).dropna()

# ----------------------------------------------------------------

st.write("## - Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur")

st.write("### **Dataset 1 :**")
df1_count = st.slider('Nombre d\'éléments à afficher :', max_value=len(df1))
st.write(df1.head(df1_count))

st.write("### **Dataset 2 :**")
df2_count = st.slider('Nombre d\'éléments à afficher :', max_value=len(df2))
st.write(df2.head(df2_count))

# ----------------------------------------------------------------

st.write("## - Afficher le nom des colonnes du dataset")

st.write("### **Dataset 1 :**")
st.write("Nom des colonnes", df1.columns)

st.write("### **Dataset 2 :**")
st.write("Nom des colonnes", df2.columns)

# ----------------------------------------------------------------

st.write("## - Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées")

st.write("### **Dataset 1 :**")
st.write("Types de colonnes : ", df1.dtypes)

st.write("### **Dataset 2 :**")
st.write("Types de colonnes : ", df2.dtypes)

# ----------------------------------------------------------------

st.write("## - La shape du dataset, par lignes et par colonnes")

st.write("### **Dataset 1 :**")
st.write("Nombre de lignes : ", str(df1.shape[0]))
st.write("Nombre de colonnes : ", str(df1.shape[1]))

st.write("### **Dataset 2 :**")
st.write("Nombre de lignes : ", str(df2.shape[0]))
st.write("Nombre de colonnes : ", str(df2.shape[1]))

# ----------------------------------------------------------------

st.write("## - Afficher les statistiques descriptives du dataset")

st.write("### **Dataset 1 :**")
st.write(df1.describe())

st.write("### **Dataset 2 :**")
st.write(df2.describe())

# ----------------------------------------------------------------

st.write("## - Affichage d'une map :")

st.write("### **Dataset 1 :**")
st.map(df1)

st.write("### **Dataset 2 :**")
st.map(df2)