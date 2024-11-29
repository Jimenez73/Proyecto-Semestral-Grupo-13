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

En el contexto de 

## <a id="Predictor-de-partidos"></a> Predictor de partidos
```
match_predictor(
    team_x=None, team_y= None, model=model_combinado, df_teams=df_teams,
    feature_names=X_train.columns.tolist()
) -> pd.DataFrame
```


``Parametros:``
- team_x: str
- team_y: str
- model: 
- df_teams: DataFrame
- feature_names: list

## <a id="BO1-BO3"></a> BO1 y BO3
```
BO1(probs_df=None) -> pd.DataFrame
```
Entrega un DataFrame de pandas donde se muestra el mapa que se jugará luego de que cada equipo elimine sus mapas más desfavorables, simulando así un enfrentamiento al mejor de uno.

``Parametros:``
- probs_df: DataFrame 

```
BO3(probs_df=None) -> pd.DataFrame
```
Entrega un DataFrame de pandas donde se muestran los tres mapas que se jugarán luego de que cada equipo elimine sus mapas más desfavorables y escoja los más favorable, simulando un enfrentamiento al mejor de tres.

``Parametros:``
- probs_df: DataFrame


## <a id="Etapas-del-Major"></a> Etapas del Major
```
Standings()
```
``Standings.add_team(team=None) -> None``

``Standings.match() -> None``

``Standings.final_results() -> None``

``Standings.simulate() -> list``

```
playoffs(teams: list) -> None
```

---

# <a id="HltvScraper"></a> Uso de HltvScraper

``def_params(self, statDate, endDate, matchType, maps, rankingFilter) -> None``

Define los headers principales para consultar información

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