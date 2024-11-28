---
layout: default
title: "Datos"
permalink: /datos/
---

# Datos utilizados

Para este proyecto se utilizaron los datos proporcionados por la página web [HLTV](https://www.hltv.org), la cual recopila todas las estadíticas de los partidos profesionales jugados. Los datos en la página están ordenados y agrupados de forma efectiva y accesible, entre estos datos están las estadísticas completas de los equipos y de sus jugadores, sumado a cada uno de los partidos jugados por todos ellos.

# Extracción de datos

(Completar)

Dado que HLTV no cuenta con una API, tuvimos que utilizar técnicas de web scraping para extraer la información. La utilización de ``cloudscraper`` para pasar la verificación de Cloudflare y ``BeautifulSoup`` para extraer la información de HTML a DataFrames de ``Pandas`` resulto primordial en este proceso.

Para este proceso se definió la clase ``HltvScraper`` con una serie de métodos para realizar una extracción de datos ordenada y reproducible por cualquier usuario. De los equipos participantes del Major, se extrajeron las estadísticas generales cada mapa junto con las estadísticas individuales de los jugadores, también organizados por mapas. Por último, se extrajeron todos los partidos jugados por lo equipos.

# Limpieza y trasformación

(Completar)

# Muestra de los Datos

(Completar)
