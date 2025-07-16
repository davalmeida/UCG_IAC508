import pandas as pd
from unit_converter import UnitConverter

def test_unit_converter():
    """
    Función de prueba para demostrar el uso de la clase UnitConverter
    """
    print("=== Prueba de la clase UnitConverter ===\n")
    
    # Crear datos de ejemplo con temperaturas en Kelvin
    data = {
        'air_temperature_k': [273.15, 283.15, 293.15, 303.15, 313.15],
        'humidity': [45, 50, 55, 60, 65],
        'pressure': [1013, 1015, 1010, 1012, 1014]
    }
    
    df = pd.DataFrame(data)
    
    print("DataFrame original:")
    print(df)
    print(f"\nTemperaturas en Kelvin: {df['air_temperature_k'].tolist()}")
    print()
    
    # Crear instancia del convertidor
    converter = UnitConverter(column_name='air_temperature_k')
    
    # Aplicar la transformación
    df_converted = converter.transform(df)
    
    print("DataFrame después de la conversión:")
    print(df_converted)
    print(f"\nTemperaturas en Celsius: {df_converted['air_temperature_k'].tolist()}")
    print()
    
    # Verificar la conversión manualmente
    print("Verificación de la conversión:")
    for i, temp_k in enumerate(data['air_temperature_k']):
        temp_c = temp_k - 273.15
        print(f"  {temp_k} K = {temp_c:.2f} °C")
    
    print("\n=== Prueba completada exitosamente ===")

def test_with_pipeline():
    """
    Demostrar cómo usar UnitConverter en un pipeline de Scikit-learn
    """
    print("\n=== Prueba con Pipeline de Scikit-learn ===\n")
    
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    
    # Crear datos de ejemplo
    data = {
        'air_temperature_k': [273.15, 283.15, 293.15, 303.15],
        'feature_1': [1, 2, 3, 4],
        'feature_2': [10, 20, 30, 40]
    }
    
    df = pd.DataFrame(data)
    print("DataFrame original:")
    print(df)
    print()
    
    # Crear pipeline con UnitConverter y StandardScaler
    pipeline = Pipeline([
        ('unit_converter', UnitConverter(column_name='air_temperature_k')),
        ('scaler', StandardScaler())
    ])
    
    # Aplicar el pipeline
    df_transformed = pipeline.fit_transform(df)
    
    print("DataFrame después del pipeline (conversión + escalado):")
    print(df_transformed)
    print("\nPipeline aplicado exitosamente!")

if __name__ == "__main__":
    # Ejecutar pruebas
    test_unit_converter()
    test_with_pipeline() 