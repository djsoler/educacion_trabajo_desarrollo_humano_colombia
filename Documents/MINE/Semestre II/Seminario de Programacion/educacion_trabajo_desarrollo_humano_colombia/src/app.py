import streamlit as st
import pandas as pd
import sys
import os

# Asegúrate de que Python reconozca la carpeta models
sys.path.append(os.path.join('C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\src\\models'))

# Importar la función de entrenamiento del modelo
from modelo_regresion import entrenar_modelo

# Título de la aplicación
st.title("Análisis de Datos de Educación para el Trabajo y el Desarrollo Humano en Colombia")

# Definir la ruta del archivo de Excel
ruta_datos = "C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\data.xlsx"

# Cargar los datos desde cada hoja con openpyxl
@st.cache_data  # Uso de la caché para mejorar el rendimiento
def cargar_datos_excel(ruta):
    try:
        data = pd.read_excel(ruta, sheet_name=None, engine='openpyxl')
        return data
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Cargar los datos desde el archivo de Excel
data = cargar_datos_excel(ruta_datos)

if data:
    # Selección de la hoja
    sheet_name = st.selectbox("Selecciona una hoja:", options=data.keys())
    df = data[sheet_name]

    # Mostrar los datos de la hoja seleccionada
    st.write(f"Datos de la hoja: {sheet_name}")
    st.write(df)

    # Botón para entrenar el modelo
    if st.button("Entrenar Modelo de Regresión Logística"):
        accuracy = entrenar_modelo()
        st.success(f"El modelo se ha entrenado con una precisión del {accuracy:.2%}")
