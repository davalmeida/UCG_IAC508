import pandas as pd

# URL del archivo CSV
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(url)

print("Dataset cargado exitosamente desde CSV!")
print(f"Forma del dataset: {df.shape}")
print("\nColumnas disponibles:")
print(df.columns.tolist())
print("\nPrimeras 5 filas:")
print(df.head()) 