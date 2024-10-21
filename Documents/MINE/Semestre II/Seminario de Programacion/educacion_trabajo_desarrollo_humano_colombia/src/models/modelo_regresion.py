# modelo_regresion.py

import sys
import os

# Asegúrate de que Python reconozca la carpeta models dentro de la ruta especificada
sys.path.append(os.path.join('C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\src\\models'))

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar los datos desde el archivo de Excel
def cargar_datos():
    ruta_datos = "C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\data.xlsx"
    instituciones = pd.read_excel(ruta_datos, sheet_name='instituciones', engine='openpyxl')
    return instituciones

# Entrenar el modelo de regresión logística
def entrenar_modelo():
    df = cargar_datos()
    
    # Suponiendo que tienes una columna 'proliferacion' que quieres predecir
    X = df.drop('proliferacion', axis=1)  # Variables independientes
    y = df['proliferacion']  # Variable dependiente

    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear el modelo
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)

    # Guardar el modelo entrenado
    with open('modelo_regresion.pkl', 'wb') as f:
        pickle.dump(modelo, f)

    # Predecir y evaluar
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

if __name__ == "__main__":
    accuracy = entrenar_modelo()
    print(f"Accuracy del modelo: {accuracy}")
