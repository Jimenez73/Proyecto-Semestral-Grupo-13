# Proyecto-Semestral-Grupo-13
Proyecto semestral del grupo 13 para el curso de Introducción a la Ciencia de Datos.

### Integrantes:

- Vicente Araya
- Sebastián Jiménez

### Página del proyecto

https://jimenez73.github.io/Proyecto-Semestral-Grupo-13/

### Explicación

En el archivo ``Modelo de predicciones Counter-Strike.pdf`` y en ``predicciones.ipynb``.

### Datos

Datos públicos sacados de la página web [HLTV](https://www.hltv.org/stats) utilizando la librería ``cloudscraper``. Los datos fueron extraidos y guardados en archivos ``.csv`` por última vez el 20/11/2024.

---

## Librerías externas utilizadas

### Librerías externas:

1. ``Pandas``
2. ``Numpy``
3. ``cloudscraper``
4. ``datetime``
5. ``time``
6. ``BeautifulSoup``
7. ``random``
8. ``seaborn``
9. ``matplotlib.pyplot``
10. ``sklearn``
11. ``xgboost``

### Librerías propias:

1. ``clase_scraper``

---

## Uso del repositorio

### Recolección de datos

En carpeta ``WebScraping`` se encuentra el el archivo ``guardar_dataframes.ipynb`` que se usó para guardar los datos scrapeados de HLTV a CSV. Además, se encuentra el archivo ``scraper_showcase.ipynb`` que muestra como usar los método más sencillos (está desactualizado para los últimos cambios pero muestra el resultado final que se quiere).

### Uso del modelo

En el notebook ``predicciones.ipynb`` se definieron funciones para usar el modelo en el contexto del Major. Se puede llamar a ``match_predictor()`` para ver las probabilidade de dos equipos en los 7 mapas. Las funciones ``BO1()`` y ``BO3()`` muestran un escenario en que dos equipos juegan un Best of 1/3 de manera de maximizar sus probabilidades. La clase ``Standings`` muestra se puede utilizar para simular una fase del torneo, y ``playoffs()`` para la fase final.