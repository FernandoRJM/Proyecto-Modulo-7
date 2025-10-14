import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo Titanic entrenado
model = joblib.load("ProyectoModulo7.pkl")

@app.route('/')
def home():
    return "API Proyecto funcionando 🚀"

# Endpoint de predicción
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Recibir JSON con los datos

        # Convertir el JSON en DataFrame
        df_prueba = pd.DataFrame([data])

        # Hacer la predicción
        prediction = model.predict(df_prueba)[0]

        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
