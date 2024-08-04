"""
se devuelve true el valor si estan duplicados y false si no estan duplicados

"""
import pandas as pd

# Crear un DataFrame con datos duplicados
data = {
    'Nombre': ['Ana', 'Luis', 'Ana', 'Luis', 'Juan', 'Pedro', 'Juan'],
    'Edad': [23, 34, 23, 34, 45, 22, 45],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

# Verificar duplicados
print("\nDatos duplicados:")
print(df.duplicated())

# Eliminar duplicados
print("\nDataFrame sin duplicados:")
limpieza = df.drop_duplicates()
print(limpieza)
