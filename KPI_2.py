import streamlit as st
import matplotlib.pyplot as plt
import pydeck as pdk
import pandas as pd

@st.cache_data
def show_kpi_2():
    st.title("KPI 2")
    
    # Crear un DataFrame de ejemplo
    data = pd.read_csv('chile.csv')
    df = pd.DataFrame(data)

    # Ejemplo de Markdown básico
    st.markdown("# Título 2")
    st.markdown("Este es un texto en **negrita** y *cursiva*.")

    # Mostrar la tabla en Streamlit
    st.dataframe(df)

    