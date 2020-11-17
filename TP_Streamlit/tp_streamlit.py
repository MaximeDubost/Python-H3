# Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import os
from streamlit.errors import Error

# Strings
str_datapath = "D:/Dataset"
str_student_name = "##### Maxime DUBOST"
str_student_group = "##### M1 IoT"
str_work_date = "##### 17/11/2020"
str_title = "Visualisation interactive des données"
str_menu = "Menu"
str_datainfo = "Description"
str_dataviz = "Visualisation"
str_select_dataset = "Sélectionnez un dataset"
str_none_dataset = "Aucun dataset sélectionné"
str_error = "Impossible d'afficher les données"
str_longitude = "longitude"
str_latitude = "latitude"
str_lon = "lon"
str_lat = "lat"
str_divider = "---"


dataset_list = os.listdir(str_datapath)
selected_menu = st.sidebar.radio(str_menu, [str_datainfo, str_dataviz])

st.write(str_student_name)
st.write(str_student_group)
st.write(str_work_date)

st.title(str_title)
selected_dataset = st.selectbox(str(), [str_select_dataset] + dataset_list)
st.write(str_divider)

if selected_menu == str_datainfo:
    st.write("## **" + str_datainfo + "**") 
if selected_menu == str_dataviz:
    st.write("## **" + str_dataviz + "**") 


try:


    if selected_dataset == str_select_dataset:
        st.warning(str_none_dataset)


    if selected_dataset != str_select_dataset:
        df = pd.read_csv("D:/Dataset/" + selected_dataset)


        # Description
        if selected_menu == str_datainfo:


            # Données
            st.write("## Données")
            try:
                line_count = st.number_input("Sélectionnez le nombre de lignes à afficher :", value=5, min_value=1, max_value=len(df))
                st.write(df.head(line_count))
            except:
                st.error(str_error)


            # Colonnes
            st.write("## Colonnes")
            try:
                st.write(df.columns)
            except:
                st.error(str_error)


            # Types des colonnes
            st.write("## Types des colonnes")
            try:
                selected_column = st.selectbox("Sélectionnez la colonne dont vous souhaitez afficher le type :", df.columns)
                st.write("La colonne **", selected_column, "** est de type ", df[selected_column].dtype)
            except:
                st.error(str_error)


            # Forme
            st.write("## Forme")
            try:
                st.write("Ce jeu de données contient **" + str(df.shape[0]) + "** ligne(s) et **" + str(df.shape[1]) + "** colonne(s)")
            except:
                st.error(str_error)


            # Statistiques descriptives
            st.write("## Statistiques descriptives")
            try:
                st.write(df.describe())
            except:
                st.error(str_error)


        # Visualisation
        if selected_menu == str_dataviz:
            

            # Heatmap
            st.write("## Heatmap")
            try:
                st.write(sns.heatmap(df.corr(), annot=True))
                st.pyplot()
            except:
                st.error(str_error)


            # Carte
            if (str_longitude in df.columns or str_lon in df.columns) and (str_latitude in df.columns or str_lat in df.columns):
                st.write("## Carte")
                try:
                    st.map(df)
                except:
                    st.error(str_error)


except:
    st.error(str_error)