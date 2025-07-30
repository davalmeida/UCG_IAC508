import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class DataPipeline:
    """
    Clase para el procesamiento de datos y entrenamiento de modelos de machine learning
    para el análisis de precios de viviendas.
    
    Esta clase proporciona métodos para preprocesar datos de viviendas, entrenar
    modelos de regresión y evaluar su rendimiento.
    
    Attributes:
        model: El modelo de machine learning entrenado (inicialmente None)
    """
    
    def __init__(self):
        """
        Inicializa una nueva instancia de DataPipeline.
        
        Crea una instancia vacía de la pipeline con el modelo inicializado como None.
        El modelo se asignará durante el proceso de entrenamiento.
        """
        self.model = None
        
    def preprocess(self, df):
        """
        Preprocesa los datos de viviendas para el entrenamiento del modelo.
        
        Realiza las siguientes transformaciones:
        1. Convierte el área de metros cuadrados a miles de metros cuadrados
        2. Crea variables dummy para las columnas categóricas
        3. Separa las características (X) del objetivo (y)
        
        Args:
            df (pandas.DataFrame): DataFrame con los datos de viviendas.
                Debe contener columnas como 'area', 'price' y columnas categóricas.
        
        Returns:
            tuple: Una tupla (X, y) donde:
                - X (pandas.DataFrame): Matriz de características preprocesadas
                - y (pandas.Series): Vector objetivo (precios de las viviendas)
        
        Raises:
            KeyError: Si el DataFrame no contiene las columnas requeridas
        """
        df = df.copy()
        df['area_miles'] = df['area'].apply(lambda x: x / 1000)
        df_dummies = pd.get_dummies(df, drop_first=True)
        X = df_dummies.drop('price', axis=1)
        y = df_dummies['price']
        return X, y
    
    def train(self, X, y, model_instance):
        """
        Entrena un modelo de machine learning con los datos proporcionados.
        
        Divide los datos en conjuntos de entrenamiento y prueba (80% - 20%),
        entrena el modelo con los datos de entrenamiento y lo almacena
        en la instancia de la clase.
        
        Args:
            X (pandas.DataFrame): Matriz de características para el entrenamiento
            y (pandas.Series): Vector objetivo (precios de las viviendas)
            model_instance: Instancia del modelo de machine learning a entrenar
                (debe tener métodos fit() y predict())
        
        Returns:
            None
            
        Note:
            El modelo entrenado se almacena en self.model y puede ser utilizado
            posteriormente para predicciones y evaluación.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model_instance.fit(X_train, y_train)
        self.model = model_instance
        print('Modelo entrenado correctamente.')

    def evaluate(self, X, y):
        """
        Evalúa el rendimiento del modelo entrenado.
        
        Calcula y muestra las métricas de rendimiento del modelo:
        - Mean Squared Error (MSE): Error cuadrático medio
        - R² Score: Coeficiente de determinación
        
        Args:
            X (pandas.DataFrame): Matriz de características para la evaluación
            y (pandas.Series): Vector objetivo real (precios de las viviendas)
        
        Returns:
            None
            
        Note:
            Si el modelo no ha sido entrenado previamente, muestra un mensaje
            de advertencia y no realiza la evaluación.
        """
        if self.model is None:
            print('El modelo no ha sido entrenado.')
            return
        y_pred = self.model.predict(X)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        print(f'MSE: {mse:.2f}')
        print(f'R2 Score: {r2:.2f}') 