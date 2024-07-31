import pandas as pd

names = ['L. Messi', 'Cristiano Ronaldo', 'Neymar Jr', 'J. Oblak', 'E. Hazard']
age = [32, 34, 27, 26, 28]
height_cm = [170, 187, 175, 188, 175]
nationality = ['Argentina', 'Portugal', 'Brazil', 'Slovenia', 'Belgium']
club = ['Paris Saint-Germain', 'Manchester United', 'Paris Saint-Germain', 'Atlético Madrid', 'Real Madrid']

# Cambiar el index a nombre
df = pd.DataFrame(index=names, data={
    'age': age, 
    'height_cm': height_cm, 
    'nationality': nationality, 
    'club': club
})

# Mostrar el DataFrame
#print(df)

# Obtener la altura y la nacionalidad de 'Cristiano Ronaldo' usando el método loc
#criss_info = df.loc['Cristiano Ronaldo', ['height_cm', 'nationality']]
#print("La altura de Cristiano Ronaldo es:", criss_info[["height_cm", "nationality"]], "cm")
#print("La nacionalidad de Cristiano Ronaldo es:", criss_info['nationality'])
#print([df.age , df.club])
print ("busqueda de ronaldo por metodo loc")
print(df.loc["Cristiano Ronaldo" ,["age","club"]])

print ("busqueda de ronaldo por metodo iloc")
print(df.iloc[1 ,[ 0 , 3]])