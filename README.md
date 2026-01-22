# Despliegue de Modelo Predictivo y Creación de API (Proyecto Final)

## 📝 Descripción
Este proyecto final integra todas las etapas del ciclo de vida de la Ciencia de Datos: desde la limpieza y el modelado hasta el despliegue funcional. Se desarrolló un modelo de Machine Learning capaz de predecir resultados basados en datos históricos, el cual se expone a través de una API para permitir consultas en tiempo real desde aplicaciones externas.

## 🛠️ Herramientas y Tecnologías
• Lenguaje: Python 3.x 
• Entorno: Jupyter Notebook / Google Colab 
• Librerías de ML: Scikit-Learn, Pandas, NumPy. 
• Despliegue y API: Flask (o FastAPI), Request handling. 
• Técnicas: Ajuste de hiperparámetros, serialización de modelos (Pickle/Joblib) y manejo de endpoints.

## 📊 Dashboard / Resultados
Tras el entrenamiento y ajuste del modelo de clasificación, se obtuvieron los siguientes resultados:

1. Desempeño del Modelo (Random Forest)
- Precisión Global (Accuracy): El modelo alcanzó un 94.3% de exactitud en la clasificación de las categorías demográficas.
- F1-Score: Se obtuvo un promedio de 0.93, demostrando un equilibrio robusto entre la precisión (capacidad de no clasificar falsos positivos) y el recall (capacidad de detectar todos los casos reales).
- Manejo de Desequilibrio: Se utilizó la técnica SMOTE (Oversampling) para compensar las clases minoritarias en el dataset, lo que permitió mejorar el rendimiento en categorías con pocos datos históricos.

2. Análisis de Datos (EDA)
- Análisis de Completitud: Se identificaron y eliminaron columnas con más del 95% de valores nulos (como birthplace_gold y religion_gold), optimizando el dataset para el modelo.
- Volumen de Datos: El estudio se realizó sobre un corpus final de 441 registros con 27 variables iniciales, filtradas para centrarse en factores demográficos esenciales.

3. Resultados de la API y Despliegue
- Disponibilidad: La API REST fue desplegada exitosamente, permitiendo consultas remotas vía método POST.
- Tiempo de Respuesta: Las pruebas de integración mostraron una latencia promedio de ~200ms por predicción.
- Confianza de Predicción: Por cada consulta, la API devuelve no solo el resultado, sino también un score de confianza superior al 90% en la mayoría de los casos de prueba.
