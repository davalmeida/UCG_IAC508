import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class UnitConverter(BaseEstimator, TransformerMixin):
    """
    Clase para convertir unidades de temperatura de Kelvin a Celsius.
    Hereda de BaseEstimator y TransformerMixin para ser compatible con pipelines de Scikit-learn.
    """
    
    def __init__(self, column_name):
        """
        Inicializa el convertidor de unidades.
        
        Parameters:
        -----------
        column_name : str
            Nombre de la columna a convertir (ej: 'air_temperature_k')
        """
        self.column_name = column_name
    
    def fit(self, X, y=None):
        """
        Método fit requerido por TransformerMixin.
        No realiza ninguna operación de entrenamiento.
        
        Parameters:
        -----------
        X : pandas.DataFrame
            DataFrame de entrada
        y : None
            No se utiliza
            
        Returns:
        --------
        self : UnitConverter
            Instancia del convertidor
        """
        return self
    
    def transform(self, X):
        """
        Convierte la temperatura de Kelvin a Celsius.
        
        Parameters:
        -----------
        X : pandas.DataFrame
            DataFrame de entrada con la columna de temperatura en Kelvin
            
        Returns:
        --------
        pandas.DataFrame
            DataFrame con la columna convertida a Celsius
        """
        # Crear una copia del DataFrame para no modificar el original
        X_transformed = X.copy()
        
        # Verificar que la columna existe
        if self.column_name not in X_transformed.columns:
            raise ValueError(f"La columna '{self.column_name}' no existe en el DataFrame")
        
        # Convertir de Kelvin a Celsius: Celsius = Kelvin - 273.15
        X_transformed[self.column_name] = X_transformed[self.column_name] - 273.15
        
        return X_transformed
    
    def fit_transform(self, X, y=None):
        """
        Combina fit y transform en una sola operación.
        
        Parameters:
        -----------
        X : pandas.DataFrame
            DataFrame de entrada
        y : None
            No se utiliza
            
        Returns:
        --------
        pandas.DataFrame
            DataFrame con la columna convertida a Celsius
        """
        return self.fit(X, y).transform(X)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear datos de ejemplo
    data = {
        'air_temperature_k': [273.15, 283.15, 293.15, 303.15],
        'other_column': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame original:")
    print(df)
    print()
    
    # Crear y usar el convertidor
    converter = UnitConverter(column_name='air_temperature_k')
    df_converted = converter.transform(df)
    
    print("DataFrame después de la conversión (Kelvin a Celsius):")
    print(df_converted) 