import pandas as pd
from tabulate import tabulate

# Datos del medallero de los Juegos Olímpicos de Río de Janeiro 2016
data = {
    'País': ['Estados Unidos', 'Reino Unido', 'China', 'Rusia', 'Alemania', 'Japón', 'Francia', 'Corea del Sur', 'Italia', 'Australia'],
    'Oro': [46, 27, 26, 19, 17, 12, 10, 9, 8, 8],
    'Plata': [37, 23, 18, 17, 10, 8, 18, 3, 12, 11],
    'Bronce': [38, 17, 26, 20, 15, 21, 14, 9, 8, 10],
    'Total': [121, 67, 70, 56, 42, 41, 42, 21, 28, 29]
}

# Crear el DataFrame
medallero_df = pd.DataFrame(data)

# Mostrar el DataFrame usando tabulate
print(tabulate(medallero_df, headers='keys', tablefmt='grid'))