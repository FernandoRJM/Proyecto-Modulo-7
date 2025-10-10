# Proyecto-Modulo-7
Proyecto 7 para el Bootcamp de Ciencia de Datos de la UDD.
Este proyecto, desarrollado como parte del Bootcamp de Ciencia de Datos e Inteligencia Artificial, se centra en el análisis de datos demográficos de los ganadores del premio Oscar de la Academia y la construcción de un modelo de Machine Learning para predecir la categoría del premio basado en estas características. Además, se implementa una API REST para permitir el acceso a las predicciones del modelo.
Objetivos del Proyecto:
- Aplicar técnicas de limpieza y análisis exploratorio de datos (EDA).
- Entrenar y evaluar un modelo de Machine Learning para clasificación.
- Realizar ajuste de hiperparámetros (tuning) para mejorar el rendimiento del modelo.
- Generar visualizaciones y métricas de rendimiento del modelo.
- Construir una API REST para servir las predicciones del modelo.
- Presentar el proyecto de manera clara y comprensible para una audiencia no técnica.

  El dataset utilizado se llama "Estadísticas demográficas de los ganadores del premio Oscar de la Academia", obtenido de Kaggle. Contiene información sobre los ganadores del Oscar, incluyendo su lugar y fecha de nacimiento, raza/etnia, religión, orientación sexual, año del premio y la categoría del premio ganado.
  Fuente del Dataset: https://www.kaggle.com/datasets/fmejia21/demographics-of-academy-awards-oscars-winners

  Metodología
El proyecto sigue los siguientes pasos:

1. Carga y Exploración de Datos: Carga del dataset y análisis inicial para comprender su estructura, identificar valores nulos y tipos de datos.
2. Limpieza de Datos: Eliminación de columnas con alta proporción de valores faltantes o irrelevantes para el análisis demográfico, y tratamiento de datos categóricos mediante codificación (Label Encoding).
3. Análisis Exploratorio de Datos (EDA): Visualización de la distribución de características clave como raza/etnia y año del premio para obtener información sobre los datos.
4. Entrenamiento del Modelo: División del dataset en conjuntos de entrenamiento y prueba y entrenamiento de un modelo de clasificación (Random Forest Classifier) para predecir la categoría del premio.
5. Evaluación del Modelo: Cálculo y visualización de métricas de rendimiento como Accuracy, Precision, Recall, F1-score y la Matriz de Confusión para evaluar la efectividad del modelo inicial.
6. Ajuste de Hiperparámetros (Tuning): Utilización de GridSearchCV para encontrar la mejor combinación de hiperparámetros para el Random Forest Classifier, buscando optimizar el rendimiento del modelo.
7. Evaluación del Modelo Ajustado: Re-evaluación del modelo con los mejores parámetros encontrados y comparación de las métricas con el modelo inicial.
8. Guardado del Modelo: Serialización del modelo entrenado y ajustado utilizando joblib para su uso posterior en la API.
9. Construcción de la API REST: Creación de un script Python utilizando Flask para exponer el modelo entrenado a través de un endpoint HTTP, permitiendo recibir datos de entrada y devolver predicciones.
10. Exposición de la API: Uso de una herramienta como Ngrok para crear un túnel seguro a la API local y hacerla accesible desde internet. (Nota: Para producción, se recomendaría una solución de despliegue en la nube).
11. Prueba de la API: Verificación del funcionamiento de la API enviando solicitudes de prueba.

Resultados
Los resultados del análisis exploratorio se presentan a través de gráficos que muestran la distribución de las características demográficas.

El rendimiento del modelo se evalúa utilizando métricas como Accuracy, Precision, Recall y F1-score, así como la Matriz de Confusión. Se comparan los resultados del modelo inicial y el modelo con hiperparámetros ajustados para analizar el impacto del tuning.

API REST
Se ha desarrollado una API REST utilizando Flask que permite obtener predicciones de la categoría del premio Oscar.

Endpoint: [URL pública de tu API] (Este URL será generado por Ngrok u otro servicio de despliegue)

Método: POST
