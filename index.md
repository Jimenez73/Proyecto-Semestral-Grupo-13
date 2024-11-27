---
layout: default
title: Inicio
---

# Bienvenido/a al Proyecto

En esta página web se explicarán las principales partes del proyecto. Aquí encontrarás una explicación general de nuestra motivación y proceso de creación del modelo. Además de una explicación más extendida del proceso de extracción, transformación y limpieza de los datos, como se escogió y preparó el modelo, y una documentación sobre el uso de los principales componentes del proyecto. 

- [Datos](datos/)
- [Modelos](modelo/)
- [Documentación](documentacion/)

# Qué es Counter-Strike 2

(Revisar)

Counter-Strike 2 o CS2 es un juego multijugador de disparos en primera persona (o FPS por sus siglas en inglés) en el cual dos equipos de cinco jugadores cada uno, se enfrentan en una partida de 24 rondas en alguno de los 7 mapas activos, donde el primero en ganar 13 de ellas se lleva la victoria. Las partidas competitivas están divididas en dos mitades de 12 rondas cada una, en la primera mitad, uno de los equipos juega como el bando antiterrorista y el otro como el bando terrorista, y en la siguiente mitad, los equipos cambian de bandos. En cada ronda los terroristas tienen como objetivo plantar una bomba en alguno de los dos puntos especiales del mapa o bien eliminarlos a todos los antiterroristas. Por otro lado, los antiterroristas tienen como objetivo defender estos puntos por la duración de la ronda, desactivar la bomba en caso de ser plantada o bien eliminar a todos los terroristas.

# Escena profesional

(Completar)

# Qué es el Major

(Completar)

# Motivación de la investigación

(Revisar)

En los próximos días comienza el Major de Counter-Strike 2 (CS2), la competencia más importante para los equipos profesionales del videojuego, con una suma de premios de 1,250,000 $USD. Este es un evento presencial y que se transmite online con miles de espectadores. Además de los premios, el evento mueve mucho dinero a través ventas en el juego de artículos exclusivos y de mercados de la comunidad con la compra y venta de recompensas por participar en las predicciones del Major, en un mini juego dentro de CS2 conocido como “Pick'em”. También se producen apuestas en páginas externas al juego.

Debido a la gran cantidad de datos que existe de los equipo y jugadores profesionales, vimos una gran oportunidad para estudiar el funcionamiento de las apuestas y cómo éstas se ven influenciadas por las distintas a características que conforman a los equipos. Esto con el fin de poder predecir con la mayor precisión posible los resultados de los partidos entre los equipos, y así tal vez poder reconocer el campeón del Major antes de que inicie el torneo principal.

# Preguntas de Investigación

(Revisar)

Nuestras preguntas iniciales fueron:

+ Variables que afectan en el juego:
    + ¿Qué factores dentro del juego tienen mayor impacto en el resultado final?
    + ¿Cómo influye el desempeño económico de cada equipo durante la partida para la predicción del resultado final?
+ Considerando selección de mapas:
    + ¿Hay cierta correlación entre los mapas elegidos y el porcentaje de victorias de cada equipo?
+ Ubicación del torneo y presencia de público:
    + ¿Hay diferencia significativa en el rendimiento de los equipos que juegan torneos virtuales y aquellos que lo hacen presencialmente?
    + ¿De qué manera influye la presencia del público en vivo el desempeño de los jugadores?

Pero un vez extraidos los datos revisados en más profundidad, nos dimos cuentas que sobre la economía durante la partida, los datos son limitados, pero existen algunos que representan en menor medida el desempeño económico del equipo, como algunas estadísticas de pistols rounds. Para realizar un análisis de reemplazo, profundizaremos más en la primera pregunta:

+ ¿Qué factores del equipo son los que más influencian el resultado?
+ ¿Qué métricas de los jugadores del equipo afectan más al porcentaje de victorias del equipo?

Esto cambia el enfoque a realizar predicciones sobre las métricas generales del equipo y sus jugadores, y no tanto así sobre las métricas individuales de cada partida. Además, sobre la ubicación y presencialidad del torneo se decidió que eran variables irrelevantes dada la naturaleza del juego. Es posible que exista algún tipo de correlación con el porcentaje de victorias del equipo, pero nuevamente, los datos sobre esto son limitados y requerirían todo un trabajo aparte que se escapa del objetivo pricipal del proyecto. Por lo tanto, se realizará un analisis de los datos sin importar que tipo de evento es y trantando de responder a preguntas sobre las posibilidades de cada equipo a ganar sobre otro

El EDA nos muestra que efectivamente hay relaciones entre las stats de los jugadores y las stats de los equipo con su porcentaje de vistorias. Esto responde a una de nuestras preguntas y confirma que la elección de mapas es importante y que la relevancia de los datos varían entre ellos. Por lo tanto, nos preguntamos: ¿Cómo varían las posibilidades de que un equipo le gane a otro dependiendo del mapa escogido?

# Objetivos

(Completar)

Creación de un modelo de predicción

# Limitaciones del modelo

(Completar)

# Conclusiones

(Completar)

Es posible predecir el campeón