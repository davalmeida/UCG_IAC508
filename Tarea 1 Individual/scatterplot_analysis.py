# DIAGRAMA DE DISPERSIÓN: Relación entre Velocidad Rotacional y Torque
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats

# Cargar el dataset (asumiendo que ya está cargado como 'df')
# Si no está cargado, descomenta las siguientes líneas:
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv"
# df = pd.read_csv(url)

# Configurar el estilo para mejor visualización
plt.style.use('default')
sns.set_palette("viridis")

# Crear figura y ejes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# === GRÁFICO 1: Scatterplot básico ===
scatter = ax1.scatter(df['rotational_speed_rpm'], df['torque_nm'], 
                     alpha=0.6, c=df['machine_failure'], 
                     cmap='RdYlBu_r', s=20)

# Personalizar el primer gráfico
ax1.set_xlabel('Velocidad Rotacional (rpm)', fontsize=12)
ax1.set_ylabel('Torque (Nm)', fontsize=12)
ax1.set_title('Relación entre Velocidad Rotacional y Torque\n(Coloreado por Fallo de Máquina)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Agregar leyenda para los colores
legend1 = ax1.legend(*scatter.legend_elements(),
                    title="Fallo de Máquina",
                    loc="upper right")
ax1.add_artist(legend1)

# === GRÁFICO 2: Scatterplot con línea de regresión ===
# Crear scatterplot con seaborn para línea de regresión
sns.regplot(data=df, x='rotational_speed_rpm', y='torque_nm', 
           ax=ax2, scatter_kws={'alpha':0.6, 's':20}, 
           line_kws={'color':'red', 'linewidth':2})

# Personalizar el segundo gráfico
ax2.set_xlabel('Velocidad Rotacional (rpm)', fontsize=12)
ax2.set_ylabel('Torque (Nm)', fontsize=12)
ax2.set_title('Relación entre Velocidad Rotacional y Torque\n(Con Línea de Regresión)', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)

# Calcular correlación y estadísticas
correlation = df['rotational_speed_rpm'].corr(df['torque_nm'])
slope, intercept, r_value, p_value, std_err = stats.linregress(df['rotational_speed_rpm'], df['torque_nm'])

# Agregar estadísticas como texto en el segundo gráfico
stats_text = f'Correlación: {correlation:.3f}\nR²: {r_value**2:.3f}\nP-valor: {p_value:.2e}\nPendiente: {slope:.4f}'
ax2.text(0.02, 0.98, stats_text, transform=ax2.transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

plt.tight_layout()
plt.show()

# === ANÁLISIS ADICIONAL ===
print("=== ANÁLISIS DE CORRELACIÓN ENTRE VELOCIDAD ROTACIONAL Y TORQUE ===")
print(f"\nCorrelación de Pearson: {correlation:.4f}")
print(f"Coeficiente de determinación (R²): {r_value**2:.4f}")
print(f"P-valor: {p_value:.2e}")
print(f"Pendiente de la línea de regresión: {slope:.4f}")
print(f"Intercepto: {intercept:.2f}")

# Interpretación de la correlación
if abs(correlation) < 0.1:
    strength = "muy débil"
elif abs(correlation) < 0.3:
    strength = "débil"
elif abs(correlation) < 0.5:
    strength = "moderada"
elif abs(correlation) < 0.7:
    strength = "fuerte"
else:
    strength = "muy fuerte"

direction = "positiva" if correlation > 0 else "negativa"
print(f"\nInterpretación: La correlación es {strength} y {direction}.")

# Estadísticas descriptivas de ambas variables
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print("\nVelocidad Rotacional (rpm):")
print(df['rotational_speed_rpm'].describe())
print("\nTorque (Nm):")
print(df['torque_nm'].describe())

# === ANÁLISIS POR TIPO DE PRODUCTO ===
print("\n=== ANÁLISIS POR TIPO DE PRODUCTO ===")
print("\nCorrelaciones por tipo de producto:")
for product_type in df['type'].unique():
    subset = df[df['type'] == product_type]
    corr = subset['rotational_speed_rpm'].corr(subset['torque_nm'])
    print(f"Tipo {product_type}: {corr:.4f}")

# === GRÁFICO ADICIONAL: Scatterplot por tipo de producto ===
fig, ax = plt.subplots(figsize=(12, 8))

colors = ['red', 'blue', 'green']
for i, product_type in enumerate(df['type'].unique()):
    subset = df[df['type'] == product_type]
    ax.scatter(subset['rotational_speed_rpm'], subset['torque_nm'], 
              alpha=0.6, s=20, label=f'Tipo {product_type}', color=colors[i])

ax.set_xlabel('Velocidad Rotacional (rpm)', fontsize=12)
ax.set_ylabel('Torque (Nm)', fontsize=12)
ax.set_title('Relación entre Velocidad Rotacional y Torque por Tipo de Producto', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show() 