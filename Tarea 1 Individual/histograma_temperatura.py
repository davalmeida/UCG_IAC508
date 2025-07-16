import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL del archivo CSV
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(url)

print("Dataset cargado exitosamente desde CSV!")
print(f"Forma del dataset: {df.shape}")

# Configurar el estilo de matplotlib para mejor visualización
plt.style.use('default')
sns.set_palette("husl")

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Crear histograma de process_temperature_k
ax.hist(df['process_temperature_k'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')

# Personalizar el gráfico
ax.set_xlabel('Temperatura del Proceso (K)', fontsize=12)
ax.set_ylabel('Frecuencia', fontsize=12)
ax.set_title('Distribución de Temperatura del Proceso', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

# Agregar estadísticas descriptivas como texto
mean_temp = df['process_temperature_k'].mean()
std_temp = df['process_temperature_k'].std()
min_temp = df['process_temperature_k'].min()
max_temp = df['process_temperature_k'].max()

stats_text = f'Media: {mean_temp:.2f} K\nDesv. Est.: {std_temp:.2f} K\nMin: {min_temp:.2f} K\nMax: {max_temp:.2f} K'
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.show()

# Mostrar estadísticas descriptivas
print("\nEstadísticas descriptivas de process_temperature_k:")
print(df['process_temperature_k'].describe()) 