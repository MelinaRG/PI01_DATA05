#Importamos 

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data import data
import pandas as pd

#Creamos la API y completamos los decoradores con las funciones que necesitamos para responder a las querys solicitadas

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index():
    return '''<html lang="en">
<head>
<title>PI DATA 05</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
.w3-sidebar {
  z-index: 3;
  width: 10px;
  top: 43px;
  bottom: 0;
  height: inherit;
}
</style>
</head>
<body>
<div class="w3-main">

  <div class="w3-row w3-padding-64">
    <div class="w3-twothird w3-container">
      <h1 class="w3-text-purple">Guía de Navegación:</h1>
      <h3>Para poder realizar una consulta debe agregar a la URL el decorador con los parametros que desea analizar, por ejemplo: </h3>
      <h4>
        <b><p>Si desea conocer la película/serie con mayor duración filtrado por plataforma, año y tipo de duración:</b>
        </h4>
      <h4 class="w3-text-purple">/get_max_duration(año, plataforma, tipo)</h4>
      <h5 class="w3-text-gray">Los parametros que puede utilizar son:</h5>
      <h5 class="w3-text-gray">Año: de 1920 a 2021</h5>
      <h5 class="w3-text-gray">Plataforma: Amazon, Disney, Hulu, Netflix</h5>
      <h5 class="w3-text-gray">Tipo: min (para peliculas), seasons (para series)</h5>
      
    </div>

  <div class="w3-row">
    <div class="w3-twothird w3-container">
      <h4>
        <b><p>Si desea conocer la cantidad de películas y de series por plataforma:</b> 
      </h4>
      <h4 class="w3-text-purple">/get_count_platform(plataforma)</h4>
      <h5 class="w3-text-gray">Los parametros que puede utilizar son:</h5>
      <h5 class="w3-text-gray">Plataforma: Amazon, Disney, Hulu, Netflix</h5>
     
    </div>

  <div class="w3-row">
    <div class="w3-twothird w3-container">
        <h4>
          <b><p>Si desea conocer la cantidad de veces que se repite un género y la plataforma con mayor frecuencia del mismo:</b> 
       </h4>
      <h4 class="w3-text-purple">/get_listedin(genero)</h4>
      <h5 class="w3-text-gray">Los parametros que puede utilizar son:</h5>
      <h5 class="w3-text-gray">Genero: Comedy, Romantic, Documentary, etc</h5>
      
    </div>

  <div class="w3-row w3-padding-64">
    <div class="w3-twothird w3-container">
        <h4>
           <b><p>Si desea conocer al actor/actriz con mayor número de apariciones según año y plataforma.</b> 
        </h4>
      <h4 class="w3-text-purple">/get_actor(plataforma, año)</h4>
      <h5 class="w3-text-gray">Los parametros que puede utilizar son:</h5>
      <h5 class="w3-text-gray">Plataforma: Amazon, Disney, Hulu, Netflix</h5>
      <h5 class="w3-text-gray">Año: de 1920 a 2021</h5>
      
    </div>
  </div>
  
<!-- END MAIN -->
</div>
</body>
</html> 
'''

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
    return (f'El titulo de mas larga duracion es: {titulo}, con un valor de {duracion} {tipo}, para la plataforma {plataforma}')

#Esta funcion nos devuelve cantidad de películas y series (separado) por plataforma 

@app.get("/get_count_plataform({plataforma})")
async def plataforma(plataforma:str):
    x = data[data['Plataforma'] == plataforma]
    x = x.groupby(['Plataforma'])['Tipo'].value_counts()
    return (f'La plataforma {plataforma} tiene {x[0]} Peliculas y {x[1]} Series')

#Esta funcion nos devuelve cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo

@app.get("/get_listedin({genero})")
async def genero(genero:str):
    x = data[data.Categoria.str.contains(genero, case=False)].groupby(by=['Plataforma']).Titulo.count()
    x= pd.DataFrame(x)
    x.reset_index(inplace=True)
    x.sort_values(by='Titulo', inplace=True, ascending=False)
    x.reset_index(inplace=True, drop=True)
    return (f'El genero {genero} se repite {x.loc[0,"Titulo"]} veces, en la plataforma {x.loc[0,"Plataforma"]} ')

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
    return f' El actor {max_actor} cuenta con {max_actor_appearances} apariciones en la plataforma {plataforma}, para el año {anio}'