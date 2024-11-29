---
layout: default
title: "Modelo"
permalink: /modelo/
---

# Elección del modelo

Este problema cae en la categoría de clasificación binaria. Por lo mismo se ordenaron los datos de ma

| Métricas   | Regresión logística | PCA y SCV  | Random Forest Regressor | Xgboost |
| ---------- | ------------------- | ---------- | ----------------------- | --------|
| RMSE       | 0.60   | 0.61   | 0.66   | 0.51   |
| Accuracy   | 0.64   | 0.62   | 0.57   | 0.74   |
| Recall     | 0.64   | 0.64   | 0.56   | 0.74   |
| Precision  | 0.63   | 0.62   | 0.57   | 0.74   |
| F score    | 0.64   | 0.63   | 0.57   | 0.74   |

# Funcionamiento del modelo

(Completar)

# Limitaciones del modelo

Durante el proceso de selección de datos y del modelo se hicieron algunos supuestos y se dejaron de lado estadísticas importantes de los equipos por la simplicidad del modelo. Algunos de estos datos son el tiempo, algunos equipos cambian de roster (jugadores activos) al terminar torneos y temporadas, lo que afecta al rendimiento del equipo. Por lo tanto, partidos jugados hace más de cierta cantidad meses pueden ya no ser representativos del equipo. Este tipo de problema se puede solucionar asignando un peso a los partidos respecto de su fecha, cambios de roster y evolución del meta. Lo que por supuesto, requiere un análisis extra para cada equipo o la creación de un modelo adicional que entregue los pesos representativos de cada partido.

Otras variables no implementadas en el modelo final, son los roles del equipo. Existen varios de ellos y por lo general, los equipos asignan a cada jugador un rol, como el IGL (in game leader), el entry fragger (encargado de entrar primero en combate) o el awper (el jugador que mejor juega con el arma AWP). Cada uno tiene un peso diferente para su equipo, lo que puede alterar las predicciones del modelo si se llegaran a implementar.

Por ejemplo, si definimos a un awper como aquellos jugadores con más de 150 Sniper kills, vemos que las estadísticas que más peso tienen para awpers y no awpers poseen varias diferencias.

![Awpers](../assets/images/stats_awpers.png)

![No-Awpers](../assets/images/stats_noawpers.png)



Como vimos, el modelo no es completamente preciso en la predicción, es decir, no nos dice quien ganará con una seguridad del 100%. Sin embargo, las métricas de precisión del modelo son lo suficientemente altas para dar estimaciones educadas sobre las chances de los equipos en todos los mapas. Lo que bajo la mirada de un individuo informado en la competición, le ayudará a realizar apuestas más precisas de los partidos.

En cuanto a las apuestas, el modelo está pensado principalmente para realizar apuestas en un juego, por lo que no presenta consecuencias negativas bajo su uso responsable y del entendimiento del análisis de los datos. Todos los datos usados son públicos, de fácil acceso y se actualizan constantemente. Además, el modelo es flexible y puede considerar datos de distintas longitudes para su uso en otras competencias.

(Explicar el cambio en la importancia de las métricas de jugadores para awpers y otros)