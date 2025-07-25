import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class DataPipeline:
    
    # Inicialización del modelo
    def __init__(self):
        self.model = None
        
    # Preprocesamiento de datos
    def preprocess(self, df):
        df = df.copy()
        df['area_miles'] = df['area'].apply(lambda x: x / 1000)
        df_dummies = pd.get_dummies(df, drop_first=True)
        X = df_dummies.drop('price', axis=1)
        y = df_dummies['price']
        return X, y
    
    # Entrenamiento del modelo
    def train(self, X, y, model_instance):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model_instance.fit(X_train, y_train)
        self.model = model_instance
        print('Modelo entrenado correctamente.')

    # Evaluación del modelo
    def evaluate(self, X, y):
        if self.model is None:
            print('El modelo no ha sido entrenado.')
            return
        y_pred = self.model.predict(X)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        print(f'MSE: {mse:.2f}')
        print(f'R2 Score: {r2:.2f}') 