# Manipulación de Duplicados en Pandas

## Crear un DataFrame con Datos Duplicados

```python
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

Verificar Duplicados

El método duplicated() devuelve una serie booleana que indica si una fila es un duplicado en comparación con las filas anteriores. Las filas que se consideran duplicadas tendrán True, y las primeras apariciones tendrán False.

python

# Verificar duplicados
print("\nDatos duplicados:")
print(df.duplicated())

Eliminar Duplicados

El método drop_duplicates() elimina las filas duplicadas del DataFrame. Si deseas modificar el DataFrame original en su lugar, usa el parámetro inplace=True.

python

# Intento de eliminar duplicados (error en el código)
print("\nDataFrame sin duplicados:")
limpieza = df.drop_duplicates
print(limpieza)

Error en el Código

En el código anterior, se olvidó agregar los paréntesis () al llamar al método drop_duplicates(). Esto no ejecuta el método y en su lugar, imprime una referencia al método.
Código Corregido

python

# Eliminar duplicados
print("\nDataFrame sin duplicados:")
limpieza = df.drop_duplicates()
print(limpieza)

Explicación de los Métodos

    df.duplicated(): Devuelve una serie booleana que indica si una fila es un duplicado.
    df.drop_duplicates(): Elimina las filas duplicadas y devuelve un nuevo DataFrame sin duplicados. Usa inplace=True para modificar el DataFrame original directamente.


Este Markdown explica el error y proporciona el código corregido para que puedas ver cómo solucionarlo. Si hay algo más que quieras ajustar o añadir, házmelo saber.
