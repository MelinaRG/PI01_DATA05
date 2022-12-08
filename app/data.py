#Importacion de las librerias que vamos a utilizar

import pandas as pd
import re

#Extraccion de los datos provenientes de 3 archivos .csv y 1 archivo .json

amazon = "./app/Datasets/amazon_prime_titles.csv"
df_1= pd.read_csv(amazon)

disney = "./app/Datasets/disney_plus_titles.csv"
df_2= pd.read_csv(disney)

hulu = "./app/Datasets/hulu_titles.csv"
df_3= pd.read_csv(hulu)

netflix = "./app/Datasets/netflix_titles.json"
df_4 = pd.read_json(netflix)

#Comenzamos con el proceso de transformacion de los datos, en este caso agregamos una columna llamada Plataforma

df_1= df_1.assign(Plataforma='Amazon')

df_2= df_2.assign(Plataforma='Disney')

df_3= df_3.assign(Plataforma='Hulu')

df_4= df_4.assign(Plataforma='Netflix')

#Concatenamos los dataframes en uno solo, para poder trabajar de manera mas eficiente y ordenada

data = pd.concat([df_1, df_2, df_3, df_4], axis=0)

#Reindexamos los indices del dataframe

data.reset_index(inplace=True)

#Eliminamos las columnas que no nos sirven para el analisis de los datos

data.drop(['index','show_id','country','date_added','rating','description'], axis=1, inplace=True)

#Tomamos una desicion con respecto a los datos nulos, en este caso los reemplazamos por 'Sin dato'

data. fillna ("Sin dato", inplace=True )

#Comprobamos que no haya filas duplicadas

data.duplicated().sum()

#Reenombramos las columnas

data.rename(columns={ 'type':'Tipo',
                        'title':'Titulo',
                        'director':'Director',
                        'cast':'Actor',
                        'release_year':'Año',
                        'duration':'Duracion',
                        'listed_in':'Categoria'}, inplace=True)

#Creamos una funcion para dejar unicamente valores int en la columna Duracion 

def extraer_num(columna):
    d = re.match(r"\d+", columna)
    if d:
      return int(d.group())
    else:
      return 0

#Aplicamos la funcion creada en la columna Duracion 

data["Duracion"] = data["Duracion"].map(extraer_num)

#Reindexamos el orden de las columnas

data.reindex(columns=['Titulo','Tipo','Año','Duracion','Categoria','Director','Actor','Plataforma'])


