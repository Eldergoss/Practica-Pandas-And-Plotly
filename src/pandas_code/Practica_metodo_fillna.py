import pandas as pd
import numpy as np

# Explicación del método fillna
"""
El método fillna permite sustituir los valores nulos de una estructura pandas por otro valor según ciertos criterios:
pueden sustituirse por un valor concreto o bien puede utilizarse el anterior o posterior valor no nulo
(en el caso de los dataframes habrá que especificar el eje sobre el que queremos aplicar la función).
"""

# Creando una Series de pandas con algunos valores NaN
print("\nSeries con valores NaN")
s = pd.Series([1, np.nan, 7, np.nan, 3])
print(s)

# Usando fillna para sustituir valores NaN por 0
print("\nSeries usando fillna para quitar valores NaN")
var = s.fillna(0)
print(var)

# Usando el método "forward fill" (ffill) para copiar los valores no nulos hacia adelante
print("\nSeries usando forward fill (ffill) para quitar valores NaN")
var2 = s.ffill()
print(var2)

# Usando el método "backward fill" (bfill) para copiar los valores no nulos hacia atrás
print("\nSeries usando backward fill (bfill) para quitar valores NaN")
var3 = s.bfill()
print(var3)

# Método fillna en DataFrames

# Crear un DataFrame con valores incluyendo NaN
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 5, 6, 7],
    'C': [8, 9, 10, np.nan]
}

# Definir el índice
index = ["luisa", "fabiola", "thor", "berserker"]

# Crear el DataFrame con los datos y el índice
df = pd.DataFrame(data, index=index)

# Rellenar valores nulos con 0
print("\nDataFrame original con valores NaN")
print(df)
df1 = df.fillna(0)
print("\nDataFrame usando fillna para cambiar valores NaN a 0")
print(df1)

# Rellenar valores nulos hacia atrás y luego rellenar cualquier NaN restante con 0
df2 = df.bfill(axis=1).fillna(0)
print("\nDataFrame usando backward fill (bfill) seguido de fillna para cambiar valores NaN")
print(df2)

# Nota: El siguiente código produce una advertencia de deprecación y no se recomienda usarlo:
# df2 = df.fillna(axis=1, method="bfill").fillna(0)
