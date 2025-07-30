# %%writefile test_my_pipeline.py
import pytest
import pandas as pd
from pipeline import DataPipeline

def test_docstrings_presence():
    """Test para verificar que todos los métodos de DataPipeline tienen docstrings"""
    pipeline = DataPipeline()
    
    # Verificar que la clase tiene docstring
    assert DataPipeline.__doc__ is not None
    assert len(DataPipeline.__doc__.strip()) > 0
    
    # Verificar que todos los métodos tienen docstrings
    methods = ['__init__', 'preprocess', 'train', 'evaluate']
    
    for method_name in methods:
        method = getattr(pipeline, method_name)
        assert method.__doc__ is not None, f"El método {method_name} no tiene docstring"
        assert len(method.__doc__.strip()) > 0, f"El método {method_name} tiene docstring vacío"
        
        # Verificar que el docstring contiene información útil
        doc = method.__doc__.lower()
        
        # Para métodos que no son __init__, verificar que documentan parámetros y retorno
        if method_name != '__init__':
            assert 'args' in doc or 'parámetros' in doc or 'param' in doc, f"El método {method_name} no documenta sus parámetros"
            assert 'return' in doc or 'devuelve' in doc, f"El método {method_name} no documenta su valor de retorno"
        else:
            # Para __init__, solo verificar que tiene documentación
            assert len(doc) > 50, f"El método {method_name} tiene documentación insuficiente"

def get_house_values(df):
    """
    Función que devuelve estadísticas de los valores de las casas
    
    Args:
        df: DataFrame con los datos de las casas
        
    Returns:
        dict: Diccionario con estadísticas de los valores de las casas
    """
    if 'price' not in df.columns:
        raise ValueError("El DataFrame debe contener una columna 'price'")
    
    values_stats = {
        'max_value': df['price'].max(),
        'min_value': df['price'].min(),
        'mean_value': df['price'].mean(),
        'median_value': df['price'].median(),
        'std_value': df['price'].std(),
        'total_houses': len(df),
        'max_value_house_index': df['price'].idxmax(),
        'min_value_house_index': df['price'].idxmin()
    }
    
    return values_stats

def test_most_valued_house():
    # Sample data similar to Housing.csv
    data = {
        'price': [100000, 250000, 175000],
        'area': [1200, 2000, 1500],
        'bedrooms': [2, 3, 2],
        'bathrooms': [1, 2, 1],
        'stories': [1, 2, 1],
        'mainroad': ['yes', 'no', 'yes'],
        'guestroom': ['no', 'yes', 'no'],
        'basement': ['no', 'no', 'yes'],
        'hotwaterheating': ['no', 'no', 'no'],
        'airconditioning': ['yes', 'no', 'yes'],
        'parking': [1, 2, 0],
        'prefarea': ['yes', 'no', 'yes'],
        'furnishingstatus': ['furnished', 'unfurnished', 'semi-furnished']
    }
    df = pd.DataFrame(data)
    pipeline = DataPipeline()
    # Preprocess to get area_miles
    X, y = pipeline.preprocess(df)
    # Find the index of the most valued house
    idx_max = y.idxmax()
    # Get area_miles for that house
    area_miles = X.loc[idx_max, 'area_miles']
    # Assert the price and area_miles are as expected
    assert y[idx_max] == 250000
    assert area_miles == 2.0

def test_most_valued_house_real_data():
    # Use the first 40 rows from the real Housing.csv
    df = pd.read_csv('/content/UCG_IAC508/Proyecto Final/Housing.csv').head(40)
    pipeline = DataPipeline()
    X, y = pipeline.preprocess(df)
    idx_max = y.idxmax()
    area_miles = X.loc[idx_max, 'area_miles']
    # The max price and area for the first 40 rows (from the csv sample)
    # Row 0: price=13300000, area=7420 -> area_miles=7.42
    # Row 1: price=12250000, area=8960 -> area_miles=8.96
    # Row 7: price=16200, area=10150000 -> area_miles=10.15 (but price is not max)
    # The max price is 13300000, area 7420, area_miles 7.42
    assert y[idx_max] == 13300000
    assert abs(area_miles - 7.42) < 1e-2

def test_get_house_values():
    """Test para la función get_house_values usando el dataset completo de Housing.csv"""
    # Cargar el dataset completo de Housing.csv
    df = pd.read_csv('/content/UCG_IAC508/Proyecto Final/Housing.csv')
    
    # Obtener estadísticas de valores
    values = get_house_values(df)
    
    # Verificar que las estadísticas son correctas según los datos reales del dataset
    assert values['max_value'] == 13300000  # Valor máximo real del dataset
    assert values['min_value'] == 1750000   # Valor mínimo real del dataset
    assert abs(values['mean_value'] - 4766729.25) < 1e-2  # Valor promedio real
    assert values['median_value'] == 4340000.0  # Valor mediano real
    assert values['total_houses'] == 545  # Total de casas en el dataset
    assert values['std_value'] > 0  # La desviación estándar debe ser positiva
    
    # Verificar que los índices están dentro del rango válido
    assert 0 <= values['max_value_house_index'] < 545
    assert 0 <= values['min_value_house_index'] < 545
    
    # Verificar que los valores en esos índices coinciden con los extremos
    assert df.loc[values['max_value_house_index'], 'price'] == 13300000
    assert df.loc[values['min_value_house_index'], 'price'] == 1750000
    
    # Verificar que la función maneja correctamente el dataset completo
    assert len(values) == 8  # Debe tener 8 estadísticas
    assert 'max_value' in values
    assert 'min_value' in values
    assert 'mean_value' in values
    assert 'median_value' in values
    assert 'std_value' in values
    assert 'total_houses' in values
    assert 'max_value_house_index' in values
    assert 'min_value_house_index' in values 
