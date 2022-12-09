
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering` :construction_worker:**</h1>

## **Introducción :paperclip:**

Les presento mi primer proyecto individual de la etapa de labs :microscope:!
En esta ocasión, les mostraré como hacer un trabajo situándome en el rol de un ***Data Engineer***, poniendo como foco central el proceso de `ETL` que es un tipo de integración de datos que hace referencia a tres pasos (extraer, transformar, cargar) que se utilizan para mezclar datos de múltiples fuentes. Por otro lado también puntualizaré en la elaboración y ejecución de una `API`, a través de **FastAPI** (un framework moderno y de alto rendimiento para construir APIs con Python).


## **Objetivo :paperclip:**

Realizar una ingesta de datos (archivos de diferentes extensiones, como *csv* o *json*), posteriormente aplicar las transformaciones pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API estará construida en un entorno virtual dockerizado.

Las consultas a realizar son:

:small_orange_diamond: Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: `get_max_duration`(año, plataforma, [min o season])

:small_orange_diamond: Cantidad de películas y series (separado) por plataforma
    El request debe ser: `get_count_plataform`(plataforma)  
  
:small_orange_diamond: Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: `get_listedin`('genero')  

:small_orange_diamond: Actor que más se repite según plataforma y año.
  El request debe ser: `get_actor`(plataforma, año)
  
## **Pasos del proyecto :paperclip:**

1:small_orange_diamond: Ingesta y normalización de datos

2:small_orange_diamond: Relacionar el conjunto de datos y crear la tabla necesaria para realizar consultas. 

3:small_orange_diamond: Leer documentación en links provistos e indagar sobre Uvicorn, FastAPI y Docker

4:small_orange_diamond: Crear la API en un entorno Docker 

5:small_orange_diamond: Realizar consultas solicitadas

6:small_orange_diamond: Realizar un video demostrativo

7:small_orange_diamond: Realizar un deployment en Mogenius 

## **Herramientas y lenguajes utilizados :paperclip:**

:small_orange_diamond: Python
:small_orange_diamond: Pandas
:small_orange_diamond: FastApi
:small_orange_diamond: HTML
:small_orange_diamond: Docker
:small_orange_diamond: Mogenius

## **Link del deployment en Mogenius: :paperclip:**

:small_orange_diamond:https://pi01-data05-prod-pi-data-50dj1r.mo2.mogenius.io/

## **Link del video explicativo: :paperclip:**

:small_orange_diamond:https://youtu.be/ho9JbrRIvlE

<a href='https://www.memegenerator.es/meme/30451188'><img src='https://cdn.memegenerator.es/imagenes/memes/full/30/45/30451188.jpg' alt='memegenerator.es' border='0'></a> Creado con <a target='_blank' href='https://www.memegenerator.es'>memegenerator.es</a>

