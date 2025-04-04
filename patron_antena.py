import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lee el archivo Excel (asegúrate de tener instalado 'openpyxl')
df = pd.read_excel("patron_radiacion_total.xlsx")

# Convierte la columna 'direccion' de grados a radianes
df['direccion_rad'] = np.deg2rad(df['Dirección Total (grados)'])

# Crea la gráfica polar
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(df['direccion_rad'], df['Magnitud Total'], c='blue', label='Datos')

# Personaliza la gráfica (título, leyenda, etc.)
ax.set_title("Gráfica de Coordenadas Polares")
ax.legend()

plt.show()
