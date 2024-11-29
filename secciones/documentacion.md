---
layout: default
title: "Documentación"
permalink: /documentacion/
---

<div id="menu-lateral" style="position: fixed; top: 150px; left: 20px; width: 230px; background: #f8f9fa; padding: 10px; border: 1px solid #ddd;">
  <strong>Esquema de la página</strong>
  <ul>
    <li><a href="#Uso-del-modelo">Uso del modelo</a></li>
      <ul>
      <li><a href="#Predictor-de-partidos">Predictor de partidos</a></li>
      <li><a href="#BO1-BO3">BO1 y BO3</a></li>
      <li><a href="#Etapas-del-Major">Etapas del Major</a></li>
    </ul>
    <li><a href="#HltvScraper">Uso de HltvScraper</a></li>
      <ul>
      <li><a href="#Stats-individuales">Stats individuales</a></li>
      <li><a href="#Stats-de-equipo">Stats de equipo</a></li>
      <li><a href="#Todos-los-equipos">Todos los equipos</a></li>
      <li><a href="#Stats-generales">Stats generales</a></li>
    </ul>
  </ul>
</div>


# <a id="Uso-del-modelo"></a> Uso del modelo

Librerías externas necesarias para utilizar el modelo:

1. ``pandas``
3. ``xgboost``

## <a id="Predictor-de-partidos"></a> Predictor de partidos
```
match_predictor(
    team_x=None, team_y= None, model=model_combinado, df_teams=df_teams,
    feature_names=X_train.columns.tolist()
) -> pd.DataFrame
```

Dado dos equipo, la función entrega estimaciones para cada equipo de ganar frente al otro en cada uno de los mapas.

``Parametros:``
- team_x: str
- team_y: str
- model: Modelo de clasificación binaria
- df_teams: pd.DataFrame
- feature_names: list

## <a id="BO1-BO3"></a> BO1 y BO3
```
BO1(probs_df=None) -> pd.DataFrame
```
Entrega un DataFrame de pandas donde se muestra el mapa que se jugará luego de que cada equipo elimine sus mapas más desfavorables, simulando así un enfrentamiento al mejor de uno.

``Parametros:``
- probs_df: pd.DataFrame 

```
BO3(probs_df=None) -> pd.DataFrame
```
Entrega un DataFrame de pandas donde se muestran los tres mapas que se jugarán, luego de que cada equipo elimine sus mapas más desfavorables y escoja los más favorable, simulando un enfrentamiento al mejor de tres.

``Parametros:``
- probs_df: pd.DataFrame


## <a id="Etapas-del-Major"></a> Etapas del Major

```
Team()
```

Clase que almacena el nombre del equipo, las victorias y las derrotas de este.

```
Nodo()
```

Clase que modela un nodo para la clase ``Standings``, en él se guardan los equipos que tienen las mismas victorias y derrotas que representa el nodo.

```
Standings()
```

Clase con estructura de grafo con Nodos y Teams, que representa la estructa de que siguen los Standings del Major.

``Standings.add_team(team: Team) -> None``

Dado un equipo, el método lo añade a primer nodo (0-0).

``Standings.match(team_x: Team, team_y: Team, BO1_: bool) -> None``

Dado dos equipos, simula quién gana y quién pierde usando el promedio de las probabilidades que obtiene de BO1 (en caso que BO1_=True) y BO3 (caso contrario). Para así moverlos al nodo correspondiente.

``Standings.simulate() -> list``

Simula todo el torneo en su totalidad siguiendo el orden en que se introducieron los equipo. Un equipo deja de jugar cuando gana 3 veces, o bien, pierde 3 veces.

``Standings.final_results() -> None``

Imprime el estado actual del grafo.

```
playoffs(teams: list) -> None
```

Función que toma los equipos de la lista en el orden dado y los enfrenta de a pares en partidos tipo BO3 (eligiendo el que gana con el promedio de las probabilidades) hasta que quede uno, imprimiendo en el proceso los partidos jugados y el ganador.

---

# <a id="HltvScraper"></a> Uso de HltvScraper

Librerías externas necesarias para utilizar HltvScraper:

1. ``Pandas``
2. ``BeautifulSoup``
3. ``cloudscraper``

``def_params(self, statDate, endDate, matchType, maps, rankingFilter) -> None``

Define los headers principales para consultar información.

``test() -> str``

- Verifica si el scraper está funcionando.

``teams_major_qualifier() -> list``

- Retorna una lista de diccionarios con los grupos de los equipos de las clasificatorias del major, con el formato "Nombre_equipo": "/id/nombre".

## <a id="Stats-individuales"></a> Stats individuales

``individual_stats(player: str, map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas individuales del jugador consultado en cierto mapa.

``career_player(player: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas anuales del Career rating 1.0 del jugador consultado.

## <a id="Stats-de-equipo"></a> Stats de equipo

``players_of_team(team: str) -> dict``

- Retorna un diccionario con los jugadores actualmente activos del equipo consultado.

``stats_players_team(team: str, map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas individuales de cada integrante del equipo consultado.

``team_stats_by_map(team: str, map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas del equipo en un mapa específico.

``matches_played(team: str) -> pd.DataFrame``

- Retorna un DataFrame con los partidos jugados por el equipo específicado.

## <a id="Todo-los-equipos"></a> Todo los equipos

``all_teams_stats_by_map(map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas de todos los equipos participantes en un mapa específico.

``all_maps_stats() -> pd.DataFrame``

- Llama a ``all_teams_stats_by_map`` para cada uno de los mapas y retorna un DataFrame con los datos.

``all_players_stats_by_team(map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas de los jugadores de todos los equipos del Major para cierto mapa.

``all_maps_players_stats() -> pd.DataFrame``

- Llama a ``all_players_stats_by_team`` para cada uno de los mapas y retorna un DataFrame con los datos.

``all_matches_played_by_team() -> pd.DataFrame``

- Retorna un DataFrame con los resultados de todos los partidos jugados por los equipo participantes del Major.

## <a id="Stats-generales"></a> Stats generales

``pistol_rounds(side: str, map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas de los equipos para las rondas de pistolas en un mapa.

``maps_pistols() -> pd.DataFrame``

- Llama a ``pistol_rounds`` para cada uno de los mapas y retorna un DataFrame con los datos.

``ftu_teams(side: str, map_name: str) -> pd.DataFrame``

- Retorna un DataFrame con las estadísticas de firepower, teamwork y utility generales de los equipos en un mapa.

``maps_ftu() -> pd.DataFrame``

- Llama a ``ftu_teams`` para cada uno de los mapas y retorna un DataFrame con los datos.