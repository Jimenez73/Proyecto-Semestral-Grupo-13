import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import cloudscraper
from datetime import date
from time import sleep

class HltvScraper():
    def __init__(self) -> None:
        self.scraper = cloudscraper.create_scraper(
            browser={"browser": "firefox", "platform": "windows"}
        )

        today = date.today()
        self.def_params(today.replace(year=2023), today, "all", "all", "all")

        self.url_base = "https://www.hltv.org"
        self.groups = ["europa_1", "europa_2", "america_rmr", "asia_rmr"]
        self.dict_maps = {
            "Ancient": 47,
            "Anubis": 48,
            "Dust2": 31,
            "Inferno": 33,
            "Mirage": 32,
            "Nuke": 34,
            "Vertigo": 46
        }
        self.dict_sides = {
            "both" : "",
            "ct": "&side=COUNTER_TERRORIST",
            "tt": "&side=TERRORIST"
        }
        self.teams_list = []

    def def_params(self, statDate, endDate, matchType, maps, rankingFilter) -> None:
        """
        Define los paremetros de consulta.
        """

        self.statDate = statDate
        self.endDate = endDate
        self.matchType = matchType
        self.maps = maps
        self.rankingFilter = rankingFilter
        
        self.params = (f"?startDate={self.statDate}&endDate={self.endDate}"
                       f"&matchType={self.matchType}&maps={self.maps}"
                       f"&rankingFilter={self.rankingFilter}")
        
    # Test

    def test(self) -> str:
        """
        Función para verificar que el scraper esté funcionando
        """
        response = self.scraper.get("https://www.hltv.org/stats")
        return f"status_code: {response.status_code}"

    # Equipos participantes

    def teams_major_qualifier(self) -> list:
        """
        Retorna una lista de diccionarios con los grupos de los equipos de las clasificatorias
        del major, con el formato "Nombre_equipo": "/id/nombre"
        """
        ulr_qualifier = "https://www.hltv.org/major/qualifier"
        response = self.scraper.get(ulr_qualifier)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return

        soup = bs(response.text, features="html.parser")
        list_team_grid = soup.find_all(class_="majorTabSection teamsGridContainer")

        list_of_groups = []

        for team_grid in list_team_grid:
            list_hrefs = team_grid.find_all("a")
            group = {}
            for href in list_hrefs:
                id = href["href"][11:]
                team = href.find(class_="text-ellipsis").text
                group[team] = id
            
            list_of_groups.append(group)

        self.teams_list = list_of_groups

        return list_of_groups
    
    # Stats individuales

    def individual_stats(self, player: str, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas individuales del jugador consultado
        en cierto mapa

        player: /id/nickname (e.g. /9816/aleksib)
        map_name: Ancient, Anubis, Dust2, Inferno, Mirage, Nuke, Vertigo
        """
        nickname = player.split("/")[2]
        map_param = f"&maps=de_{map_name.lower()}"

        url_team = self.url_base + "/stats/players/individual" + player + self.params + map_param
        response = self.scraper.get(url_team)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"
        
        soup = bs(response.text, features="html.parser")
        tabla = soup.find(class_="columns")
        list_standard_box = tabla.find_all(class_="standard-box")

        stats = {}

        for box in list_standard_box:
            for row in box.find_all(class_="stats-row"):
                labels = [span.text for span in row.find_all('span')]
                stats[labels[0]] = labels[-1]


        df = pd.DataFrame(stats, index=[0])
        df["Player"] = nickname
        
        return df

    def career_player(self, player: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas anuales del Career rating 1.0 del 
        jugador consultado

        player: /id/nickname (e.g. /9816/aleksib)
        """
        ulr_career = self.url_base + "/stats/players/career" + player
        response = self.scraper.get(ulr_career)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"

        soup = bs(response.text, features="html.parser")
        table = soup.find(class_="stats-table")
        table = table.find_all("tr")

        label_cols = table[0].find_all("th")
        label_cols = [col.text for col in label_cols]

        df = pd.DataFrame(columns=label_cols)

        for row in table[1:-1]:
            cols = row.find_all("td")
            cols = [col.text for col in cols]

            df_temp = pd.DataFrame(data=[cols], columns=label_cols)
            
            df = pd.concat([df, df_temp], axis=0)

        df = df.replace("-", np.nan)
        
        return df

    # Stats de equipo

    def players_of_team(self, team: str) -> dict:
        """
        team: /id/nombre (e.g. /4608/natus-vincere)
        """

        url_team = self.url_base + "/stats/teams/" + team + self.params
        response = self.scraper.get(url_team)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"

        soup = bs(response.text, features="html.parser")
        list_reset_grid = soup.find_all(class_="grid reset-grid")
        list_team_info = list_reset_grid[0].find_all(class_="teammate-info standard-box")

        players = {}
        for box in list_team_info:
            link = box.find("a")["href"]
            teammate = box.find(class_="text-ellipsis").text

            players[teammate] = link

        return players

    def stats_players_team(self, team: str, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas individuales de cada integrante del
        equipo consultado.

        team: /id/nombre (e.g. /4608/natus-vincere)
        map_name: Ancient, Anubis, Dust2, Inferno, Mirage, Nuke, Vertigo
        """
        df_players = pd.DataFrame()
        dict_players = self.players_of_team(team)

        counter = 0
        while dict_players == "Error" and counter < 10:
            sleep(1)
            print("Reintentando hacer request...")
            dict_players = self.players_of_team(team)
            counter += 1

        if dict_players == "Error":
            return "Error"

        for link in dict_players.values():
            player = link.split("?")[0][14:]
            df = self.individual_stats(player, map_name)
            df_players = pd.concat([df_players, df])
            sleep(0.5)
            
        return df_players

    def team_stats_by_map(self, team: str, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas del equipo en un mapa específico.

        team: /id/nombre (e.g. /4608/natus-vincere)
        map_name: Ancient, Anubis, Dust2, Inferno, Mirage, Nuke, Vertigo
        """
        try:
            id_map = self.dict_maps[map_name]
        except KeyError as error:
            print("El nombre ingresado no es valido")
            raise error

        url_map = f"{self.url_base}/stats/teams/map/{id_map}/{team}{self.params}"
        response = self.scraper.get(url_map)

        if response.status_code != 200:
            return f"Error {response.status_code}"

        soup = bs(response.text, features="html.parser")

        table = soup.find(class_="stats-rows standard-box")
        table = table.find_all(class_="stats-row")

        map_stats = {}
        for row in table:
            labels = [span.text for span in row.find_all('span')]
            map_stats[labels[0]] = labels[1]

        df = pd.DataFrame(data=map_stats, index=[0])
        return df

    def matches_played(self, team: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con los partidos jugados por el equipo específicado.

        team: /id/nombre (e.g. /4608/natus-vincere)
        """
        url = self.url_base + "/stats/teams/matches/" + team + self.params
        response = self.scraper.get(url)

        if response.status_code != 200:
            return f"Error {response.status_code}"

        soup = bs(response.text, features="html.parser")
        table = soup.find(class_="stats-table no-sort")

        df = pd.DataFrame(columns=["Date", "Event", "Opponent", "Map", "Result", "W/L"])

        for row in table.find_all('tr')[1:]:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            cols.pop(2)
            new_row = pd.DataFrame([cols], columns=df.columns)

            df = pd.concat([df, new_row], ignore_index=True, axis=0)

        return df 

   # Stats de todo los team participantes

    def all_teams_stats_by_map(self, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas de todos los equipos participantes 
        en un mapa específico.

        map_name: Ancient, Anubis, Dust2, Inferno, Mirage, Nuke, Vertigo
        """
        all_teams = pd.DataFrame()

        if not self.teams_list:
            self.teams_list = self.teams_major_qualifier()

        for teams_dict, group in zip(self.teams_list, self.groups):
            for team, link in teams_dict.items():
                df = self.team_stats_by_map(link, map_name)
                df["Group"] = group
                df["Team"] = team
                all_teams = pd.concat([all_teams, df])

                # Es importante detener el un tiempo el loop para evitar el error 429
                sleep(0.5)

        return all_teams
    
    def all_maps_stats(self) -> pd.DataFrame:
        df_maps = pd.DataFrame()

        for map_name in self.dict_maps.keys():
            df = self.all_teams_stats_by_map(map_name=map_name)
            df["Map Name"] = map_name
            df_maps = pd.concat([df_maps, df])
            sleep(0.5)

        return df_maps

    def all_players_stats_by_team(self, map_name: str) -> pd.DataFrame:
        all_teams = pd.DataFrame()

        if not self.teams_list:
            self.teams_list = self.teams_major_qualifier()

        for teams_dict, group in zip(self.teams_list, self.groups):
            for team, link in teams_dict.items():
                df = self.stats_players_team(link, map_name)
                df["Group"] = group
                df["Team"] = team
                all_teams = pd.concat([all_teams, df])

        return all_teams

    def all_maps_players_stats(self) -> pd.DataFrame:
        df_maps = pd.DataFrame()

        for map_name in self.dict_maps.keys():
            df = self.all_players_stats_by_team(map_name)
            df["Map Name"] = map_name
            df_maps = pd.concat([df_maps, df])

        return df_maps

    def all_matches_played_by_team(self) -> pd.DataFrame:
        all_teams = pd.DataFrame()

        if not self.teams_list:
            self.teams_list = self.teams_major_qualifier()

        for teams_dict, group in zip(self.teams_list, self.groups):
            for team, link in teams_dict.items():
                df = self.matches_played(link)
                df["Group"] = group
                df["Team"] = team
                all_teams = pd.concat([all_teams, df])

                sleep(0.5)

        return all_teams

    # Stats generales

    def pistol_rounds(self, side: str, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas anuales de los equipos para las
        rondas de pistolas.

        side: side ("both", "ct" "tt")
        map_name: Ancient, Anubis, Dust2, Inferno, Mirage, Nuke, Vertigo
        """
        try:
            side_param = self.dict_sides[side]
        except KeyError as error:
            print("El side ingresado no es valido")
            raise error
        
        map_param = f"&maps=de_{map_name.lower()}"
        
        url_pistol_round = self.url_base + "/stats/teams/pistols" + self.params + side_param + map_param + "&minMapCount=0"
        response = self.scraper.get(url_pistol_round)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"
        
        soup_pistol_round = bs(response.text, features="html.parser")
        info_pistol_round = soup_pistol_round.find(class_="stats-table player-ratings-table ftu")
        table = info_pistol_round.find_all("tr")

        label_cols = table[0].find_all("th")
        label_cols = [col.text for col in label_cols]

        df = pd.DataFrame(columns=label_cols)

        for row in table[1:]:
            cols = row.find_all("td")
            cols = [col.text for col in cols]

            df_temp = pd.DataFrame(data=[cols], columns=label_cols)        
            df = pd.concat([df, df_temp], axis=0)

        df = df.reset_index(drop=True)
        df = df.rename(columns={"Round 2 convR2 conv": "Round 2 conv", "Round 2 breakR2 break": "Round 2 break"})
        return df

    def ftu_teams(self, side: str, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas ftu generales de los equipos.

        side: side ("both", "ct" "tt")
        map_name: Ancient, Anubis, Dust2, Inferno, Mirage, Nuke, Vertigo
        """
        try:
            side_param = self.dict_sides[side]
        except KeyError as error:
            print("El side ingresado no es valido")
            raise error
        
        map_param = f"&maps=de_{map_name.lower()}"
        
        url_pistol_round = self.url_base + "/stats/teams/ftu" + self.params + side_param + map_param + "&minMapCount=0"
        response = self.scraper.get(url_pistol_round)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"
        
        soup = bs(response.text, features="html.parser")
        table = soup.find(class_="stats-table player-ratings-table ftu gtSmartphone-only")

        df = pd.DataFrame(columns=["Team", "Maps", "RW%", "OpK", "MultiK", "5v4%", "4v5%", "Traded%", "ADR", "FA"])

        for row in table.find_all('tr')[2:]:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            
            new_row = pd.DataFrame([cols], columns=df.columns)

            df = pd.concat([df, new_row], ignore_index=True, axis=0)

        return df
    
    def maps_pistols(self) -> pd.DataFrame:
        df_maps = pd.DataFrame()

        for map_name in self.dict_maps.keys():
            df = self.pistol_rounds("both", map_name)
            df["Map Name"] = map_name
            df_maps = pd.concat([df_maps, df])

        return df_maps

    def maps_ftu(self) -> pd.DataFrame:
        df_maps = pd.DataFrame()

        for map_name in self.dict_maps.keys():
            df = self.ftu_teams("both", map_name)
            df["Map Name"] = map_name
            df_maps = pd.concat([df_maps, df])

        return df_maps