import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Cargamos el archivo de datos
movies_path = 'pelis_vistas.csv'
movies = pd.read_csv(movies_path, delimiter=';')

#Comprobamos que el archivo es correcto
#print(movies.head())

#Convertimos todo a minusculas para evitar problemas con las mayusculas
movies['Nombre'] = movies['Nombre'].str.lower()
movies['Director'] = movies['Director'].str.lower()
movies['Protagonista'] = movies['Protagonista'].str.lower()
movies['Genero'] = movies['Genero'].str.lower()
movies['Pais'] = movies['Pais'].str.lower()

#Procesamos los datos:

#Opción 1 (Pocos directores y actores): Crear variables dummy para los directores y actores
#movies_directores = pd.get_dummies(movies['Director'], prefix="dir")
#movies_protagonistas = pd.get_dummies(movies['Protagonista'], prefix="prot")
#movies = pd.concat([movies, movies_directores, movies_protagonistas], axis=1)
#movies_genero = pd.get_dummies(movies['Genero'], prefix="gen")
#movies_pais = pd.get_dummies(movies['Pais'], prefix="pais")
#movies = pd.concat([movies, movies_directores, movies_protagonistas, movies_genero, movies_pais], axis=1)

#Opción 2 (Muchos directores y actores): Usar LabelEncoder para los directores y actores
le = LabelEncoder()
movies['Director'] = le.fit_transform(movies['Director'])
movies['Protagonista'] = le.fit_transform(movies['Protagonista'])
movies['Genero'] = le.fit_transform(movies['Genero'])
movies['Pais'] = le.fit_transform(movies['Pais'])


print(movies.head())