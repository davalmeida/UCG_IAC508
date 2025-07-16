import pandas as pd
from unit_converter import UnitConverter

def demo_unit_converter():
    """
    Demostración de la creación de una instancia de UnitConverter
    y su aplicación a un DataFrame
    """
    print("=== Demostración de UnitConverter ===\n")
    
    # Crear un DataFrame de ejemplo con temperaturas en Kelvin
    data = {
        'air_temperature_k': [273.15, 283.15, 293.15, 303.15, 313.15, 323.15, 333.15],
        'humidity': [45, 50, 55, 60, 65, 70, 75],
        'pressure': [1013, 1015, 1010, 1012, 1014, 1016, 1018],
        'wind_speed': [5.2, 6.1, 4.8, 7.3, 5.9, 6.7, 8.1]
    }
    
    df = pd.DataFrame(data)
    
    print("1. DataFrame original (primeras 5 filas):")
    print(df.head())
    print()
    
    print("2. Creando instancia de UnitConverter...")
    # Crear instancia de UnitConverter para la columna 'air_temperature_k'
    converter = UnitConverter(column_name='air_temperature_k')
    print(f"   Convertidor creado para la columna: '{converter.column_name}'")
    print()
    
    print("3. Aplicando transformación...")
    # Aplicar la transformación
    df_converted = converter.transform(df)
    print("   Transformación completada!")
    print()
    
    print("4. DataFrame después de la conversión (primeras 5 filas):")
    print(df_converted.head())
    print()
    
    print("5. Verificación de la conversión:")
    print("   Comparando valores originales vs convertidos:")
    for i in range(5):
        original_k = df.iloc[i]['air_temperature_k']
        converted_c = df_converted.iloc[i]['air_temperature_k']
        expected_c = original_k - 273.15
        print(f"   Fila {i}: {original_k:.2f} K → {converted_c:.2f} °C (esperado: {expected_c:.2f} °C)")
    
    print("\n6. Verificación de que otras columnas no cambiaron:")
    print("   Columnas originales:", list(df.columns))
    print("   Columnas después de conversión:", list(df_converted.columns))
    print("   ¿Las columnas son iguales?", list(df.columns) == list(df_converted.columns))
    
    # Verificar que las columnas no convertidas mantienen sus valores
    other_columns = ['humidity', 'pressure', 'wind_speed']
    for col in other_columns:
        if (df[col] == df_converted[col]).all():
            print(f"   ✓ Columna '{col}' mantiene sus valores originales")
        else:
            print(f"   ✗ Columna '{col}' ha sido modificada")
    
    print("\n=== Demostración completada exitosamente ===")

if __name__ == "__main__":
    demo_unit_converter() 