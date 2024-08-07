"""
Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" que contiene
los nombres de los alumnos y sus calificaciones en varias materias. Luego, agrega una
columna llamada "Mat_Fisica" que contiene valores aleatorios entre 0 y 100 con un decimal
y guarda el archivo con la nueva columna.
"""

import pandas as pd
import numpy as np

# Leer el archivo Excel
archivo_excel = "calificaciones_alumnos.xlsx"
df = pd.read_excel(archivo_excel)

# Generar valores aleatorios entre 0 y 100 con un decimal para la columna "Mat_Fisica"
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, len(df)), 1)

# Guardar el DataFrame modificado de nuevo en el archivo Excel
df.to_excel(archivo_excel, index=False)

print("Se ha agregado la columna 'Mat_Fisica' con valores aleatorios entre 0 y 100.")