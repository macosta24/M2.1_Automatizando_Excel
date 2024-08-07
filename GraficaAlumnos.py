"""
Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" que contiene
los nombres de los alumnos y sus calificaciones en varias materias. Luego, grafica
estas calificaciones en un gráfico de barras para cada alumno, asegurándose de que
las etiquetas en el eje X no se encimen.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
archivo_excel = "calificaciones_alumnos.xlsx"
df = pd.read_excel(archivo_excel)

# Seleccionar columnas de interés
columnas_calificaciones = ['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Iterar sobre cada columna de calificación para crear una serie de barras
for idx, columna in enumerate(columnas_calificaciones):
    # Ajustar las posiciones de las barras para que no se encimen
    posiciones = [i + idx*0.2 for i in range(len(df))]
    ax.bar(posiciones, df[columna], width=0.2, label=columna)

# Configurar las etiquetas del eje X
ax.set_xticks([i + 0.2 for i in range(len(df))])
ax.set_xticklabels(df['Nombre'], rotation=45, ha='right')

# Agregar leyenda
ax.legend()

# Agregar títulos y etiquetas
ax.set_title('Calificaciones de los Alumnos')
ax.set_xlabel('Alumnos')
ax.set_ylabel('Calificaciones')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
