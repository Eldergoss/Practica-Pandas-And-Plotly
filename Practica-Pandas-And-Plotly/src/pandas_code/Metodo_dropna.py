"""El método dropna permite, de una forma muy conveniente,
filtrar los valores de una estructura de datos pandas para dejar solo aquellos no nulos."""

import pandas as pd
import numpy as np

# Definición del DataFrame
ventas = pd.DataFrame({
    "A": [1, 5, 4, 7],
    "B": [3, 4, 1, np.nan],
    "C": [3, 7, 2, 1],
    "D": [np.nan, 2, 2, 3]
}, index=["Ene", "Feb", "Mar", "Abr"])

# Eliminar filas con cualquier valor NaN
df_cleaned = ventas.dropna()
print("DataFrame sin filas con valores NaN:")
print(df_cleaned)

# Eliminar columnas con cualquier valor NaN
df_cleaned2 = ventas.dropna(axis=1)
print("\nDataFrame sin columnas con valores NaN:")
print(df_cleaned2)

"""Mediante el parámetro how podemos controlar cómo queremos que se aplique el método: 
si toma el valor "all", solo se eliminarán las filas o columnas en las que todos sus elementos sean nulos.
Si toma el valor "any" (valor por defecto)
se eliminarán las filas o columnas en las que algún elemento sea nulo. De esta forma:"""
print("\nDataFrame usando dropna y how  e all")
df_cleaned4 = ventas.dropna(how = "all")
print(df_cleaned4)

print("\nDataFrame usando dropna y how  e any")
df_cleaned5 = ventas.dropna(how = "any")
print(df_cleaned5)