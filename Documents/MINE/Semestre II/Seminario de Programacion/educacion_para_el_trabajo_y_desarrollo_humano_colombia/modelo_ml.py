# modelo_ml.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Datos de ejemplo
data = {
    'horas_estudio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'pasa_examen': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Separar las características (X) y la variable objetivo (y)
X = df[['horas_estudio']]
y = df['pasa_examen']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de regresión logística
modelo = LogisticRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

# Calcular la precisión del modelo
precision = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {precision * 100:.2f}%')
