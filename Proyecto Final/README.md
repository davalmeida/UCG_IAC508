# Proyecto Final: Predicción de Precios de Viviendas

## Descripción del Proyecto

Este proyecto implementa un pipeline de machine learning para predecir precios de viviendas utilizando programación orientada a objetos (POO) y buenas prácticas de desarrollo de software.

## Estructura del Proyecto

```
Proyecto Final/
├── Proyecto_Final.ipynb          # Notebook principal con el análisis
├── pipeline.py                   # Clase DataPipeline implementada
├── test_mi_pipeline.py          # Pruebas unitarias con pytest
├── requirements.txt              # Dependencias del proyecto
├── Housing.csv                   # Dataset de precios de viviendas
└── README.md                     # Este archivo
```

## Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el análisis completo
Abre el notebook `Proyecto_Final.ipynb` en Jupyter o Google Colab.

### Ejecutar las pruebas
```bash
python -m pytest test_mi_pipeline.py -v
```

## Clase DataPipeline

La clase `DataPipeline` implementa un pipeline completo de machine learning con los siguientes métodos:

### `__init__()`
Inicializa la instancia del pipeline.

### `preprocess(df)`
Preprocesa los datos:
- Agrega la columna `area_miles` (área en miles)
- Convierte variables categóricas a variables dummy
- Separa features (X) y target (y)

**Parámetros:**
- `df`: DataFrame con los datos originales

**Retorna:**
- `X`: DataFrame con las features preprocesadas
- `y`: Series con la variable objetivo

### `train(X, y, model_instance)`
Entrena el modelo especificado:
- Divide los datos en train/test (80/20)
- Entrena el modelo con los datos de entrenamiento
- Guarda el modelo entrenado

**Parámetros:**
- `X`: Features preprocesadas
- `y`: Variable objetivo
- `model_instance`: Instancia del modelo a entrenar

### `evaluate(X, y)`
Evalúa el modelo entrenado:
- Calcula predicciones
- Muestra MSE y R² Score

**Parámetros:**
- `X`: Features para evaluación
- `y`: Valores reales

## Pruebas Unitarias

El archivo `test_mi_pipeline.py` contiene pruebas unitarias que verifican:

1. **`test_preprocess_agrega_area_miles`**: Verifica que se agregue correctamente la columna `area_miles`
2. **`test_preprocess_convierte_categoricas_a_dummy`**: Verifica la conversión de variables categóricas
3. **`test_train_method`**: Verifica el funcionamiento del método de entrenamiento
4. **`test_evaluate_method`**: Verifica el funcionamiento del método de evaluación

## Dataset

El dataset `Housing.csv` contiene información sobre viviendas con las siguientes columnas:
- `price`: Precio de venta (variable objetivo)
- `area`: Área en pies cuadrados
- `bedrooms`: Número de dormitorios
- `bathrooms`: Número de baños
- `stories`: Número de pisos
- `mainroad`: Si está en carretera principal (yes/no)
- `guestroom`: Si tiene cuarto de huéspedes (yes/no)
- `basement`: Si tiene sótano (yes/no)
- `hotwaterheating`: Si tiene calefacción de agua (yes/no)
- `airconditioning`: Si tiene aire acondicionado (yes/no)
- `parking`: Número de espacios de estacionamiento
- `prefarea`: Si está en área preferencial (yes/no)
- `furnishingstatus`: Estado del amueblado (furnished/unfurnished/semi-furnished)

## Resultados

El modelo de regresión lineal alcanza:
- **MSE**: 1,125,550,288,218.71
- **R² Score**: 0.68

## Tecnologías Utilizadas

- **Python**: Lenguaje principal
- **Pandas**: Manipulación de datos
- **Scikit-learn**: Machine learning
- **Pytest**: Testing unitario
- **Matplotlib/Seaborn**: Visualización
- **Jupyter Notebook**: Análisis interactivo

## Autor

Desarrollado como proyecto final para el curso de Inteligencia Artificial y Ciencia de Datos. 