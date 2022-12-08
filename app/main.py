#Importamos 

from fastapi import FastAPI
from data import data
import pandas as pd

#Creamos la API y completamos los decoradores con las funciones que necesitamos para responder a las querys solicitadas

app = FastAPI()

@app.get('/')
async def mensaje():
    'Bienvenidos'

#Esta funcion nos devuelve la máxima duración según tipo de film (película/serie) 

@app.get("/get_max_duration({anio}, {plataforma}, {tipo})")
async def duracion(anio:int, plataforma:str, tipo:str):
    if tipo == 'min':
        t = 'Movie'
        x = data[data['Plataforma'] == plataforma][data['Año'] == anio][data['Tipo'] == t].groupby(['Plataforma', 'Tipo', 'Año'])['Duracion'].idxmax()
        duracion = data['Duracion'].get(x[0])
        titulo = data['Titulo'].get(x[0])
    if tipo == 'seasons':
        t = 'TV Show'
        x = data[data['Plataforma'] == plataforma][data['Año'] == anio][data['Tipo'] == t].groupby(['Plataforma', 'Tipo', 'Año'])['Duracion'].idxmax()
        duracion = data['Duracion'].get(x[0]) 
        titulo = data['Titulo'].get(x[0])
    return (f'El titulo de mas larga duracion es: {titulo}, con un valor de {duracion}')

#Esta funcion nos devuelve cantidad de películas y series (separado) por plataforma 

@app.get("/get_count_plataform({plataforma})")
async def plataforma(plataforma:str):
    x = data[data['Plataforma'] == plataforma]
    x = x.groupby(['Plataforma'])['Tipo'].value_counts()
    return x

#Esta funcion nos devuelve cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo

@app.get("/get_listedin({genero})")
async def genero(genero:str):
    x = data[data.Categoria.str.contains(genero, case=False)].groupby(by=['Plataforma']).Titulo.count()
    x= pd.DataFrame(x)
    x.reset_index(inplace=True)
    x.sort_values(by='Titulo', inplace=True, ascending=False)
    x.reset_index(inplace=True, drop=True)
    return x.iloc[0]

#Esta funcion nos devuelve actor que más se repite según plataforma y año

@app.get("/get_actor({plataforma}, {anio})")
async def actor(plataforma:str, anio:int):
    actor_list = []
    cast_list = data.query(f"Plataforma == '{plataforma}' and Año == {anio}").Actor.tolist()
    for i in range(len(cast_list)):
        actor_list_temp = cast_list[i].split(",")
        for j in range(len(actor_list_temp)):
            if actor_list_temp[j] != 'Sin dato':
                actor_list.append(actor_list_temp[j])
    dict_actor = dict(zip(actor_list,map(lambda x: actor_list.count(x),actor_list)))
    max_actor = max(dict_actor, key=dict_actor.get)
    max_actor_appearances = dict_actor.get(max_actor)
    return f' El actor {max_actor} cuenta con {max_actor_appearances} apariciones.'