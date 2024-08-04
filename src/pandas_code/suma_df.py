import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Imprimir el DataFrame
print("\nDataFrame:")
print(df)


# Imprimir un mensaje con salto de línea antes
print("\nSumar los valores a lo largo de las columnas")
suma_columnas = df.sum(axis=0)
print(suma_columnas)

# Imprimir otro mensaje con salto de línea antes
print("\nSumar los valores a lo largo de las filas")
suma_filas = df.sum(axis=1)
print(suma_filas)

