# ejecutar_modelo.py

import pandas as pd
import pickle

# Cargar el modelo
with open('modelo_regresion.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Cargar los datos (puedes modificar esta parte para que reciba datos externos)
ruta_datos = "C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\data.xlsx"
df = pd.read_excel(ruta_datos, sheet_name='instituciones', engine='openpyxl')

# Suponiendo que tienes un conjunto de datos preparado para hacer predicciones
X_nuevos_datos = df.drop('proliferacion', axis=1)  # Variables independientes

# Hacer predicciones
predicciones = modelo.predict(X_nuevos_datos)

# Mostrar resultados
print("Predicciones:", predicciones)
