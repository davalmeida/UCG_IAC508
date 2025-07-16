import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# URL del archivo CSV
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(url)

print("Dataset cargado exitosamente desde CSV!")
print(f"Forma del dataset: {df.shape}")

# Limpiar nombres de columnas
def clean_column_name(column_name):
    import re
    clean_name = column_name.lower()
    clean_name = re.sub(r'[^a-zA-Z0-9\s]', ' ', clean_name)
    clean_name = re.sub(r'\s+', '_', clean_name)
    clean_name = clean_name.strip('_')
    return clean_name

# Aplicar la función para renombrar todas las columnas
df.columns = [clean_column_name(col) for col in df.columns]

print("\nColumnas disponibles:")
print(df.columns.tolist())

# Extraer las series específicas para evitar problemas de tipo
rotational_speed = df['rotational_speed_rpm'].astype(float)
torque = df['torque_nm'].astype(float)

# Crear el scatter plot
plt.figure(figsize=(12, 8))

# Crear scatter plot con seaborn
sns.scatterplot(data=df, x='rotational_speed_rpm', y='torque_nm', 
                alpha=0.6, s=30, color='steelblue')

# Personalizar el gráfico
plt.xlabel('Velocidad de Rotación (rpm)', fontsize=12)
plt.ylabel('Torque (Nm)', fontsize=12)
plt.title('Relación entre Velocidad de Rotación y Torque', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Calcular correlación usando numpy para evitar problemas de tipo
correlation_matrix = np.corrcoef(rotational_speed, torque)
correlation = correlation_matrix[0, 1]
r_squared = correlation ** 2

# Agregar línea de tendencia
z = np.polyfit(rotational_speed, torque, 1)
p = np.poly1d(z)
plt.plot(rotational_speed, p(rotational_speed), 
         "r--", alpha=0.8, linewidth=2, label=f'Tendencia (r² = {r_squared:.3f})')

# Agregar estadísticas de correlación
stats_text = f'Correlación: {correlation:.3f}\nR²: {r_squared:.3f}'
plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.legend()
plt.tight_layout()

# Guardar y mostrar el gráfico
plt.savefig('scatter_plot_rotational_speed_torque_fixed.png', dpi=300, bbox_inches='tight')
plt.show()

# Mostrar estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print("=" * 50)
print("Velocidad de Rotación (rpm):")
print(rotational_speed.describe())
print("\nTorque (Nm):")
print(torque.describe())
print(f"\nCorrelación entre variables: {correlation:.3f}")
print(f"Coeficiente de determinación (R²): {r_squared:.3f}")

# Verificar que no hay valores nulos
print(f"\nValores nulos en velocidad de rotación: {rotational_speed.isnull().sum()}")
print(f"Valores nulos en torque: {torque.isnull().sum()}") 