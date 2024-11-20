# NO SUBIR CAMBIOS A MAIN
## USAR RAMA `cambios_por_aprobar`

# Proyecto-Semestral-Grupo-13
Proyecto semestral del grupo 13 para el ramo Intro a la Cs de Datos

### Integrantes:

- Vicente Araya
- Aldo Coello
- Sebastián Jiménez
- Carolina Neira

### Explicación

En el archivo ``Modelo de predicciones Counter-Strike.pdf``

### Datos

Datos públicos sacados de la página web [HLTV](https://www.hltv.org/stats) utilizando la librería ``cloudscraper``. Los datos fueron extraidos y guardados en archivos ``.csv`` por última vez el 20/11/2024.

---

## Cosas por hacer

### ETL

- Terminar los métodos de extracción de datos
- Extraer todas la información que necesitamos
- Juntarlos DataFrames en uno solo según corresponda para jugadores y para equipos (🛑 Estamos aquí)
- Limpiar los datos
    - Datos nulos
    - Datos duplicados
    - Formato correcto (Dtypes)

### EDA

- Identificar las variables que afectan a las victorias del equipo

### Modelo

- Crear un modelo que prediga los efrentamientos entre equipos

---

### Librerías externas utilizadas
La lista de librerías utilizadas:

1. ``Pandas``
2. ``Numpy``
3. ``cloudscraper``
4. ``datetime``
5. ``time``
6. ``BeautifulSoup``

### Librerías propias

1. ``clase_scraper``
