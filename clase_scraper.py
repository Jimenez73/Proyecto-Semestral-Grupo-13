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
        self.url_base = "https://www.hltv.org"

        today = date.today()
        self.def_params(today.replace(year=2023), today, "all", "all", "all")

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
    
    def individual_stats(self, player: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas individuales del jugador consultado

        player: /id/nickname (e.g. /9816/aleksib)
        """

        nickname = player.split("/")[2]
        url_team = self.url_base + "/stats/players/individual" + player + self.params
        response = self.scraper.get(url_team)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"
        
        soup = bs(response.text, features="html.parser")
        tabla = soup.find(class_="columns")
        list_standard_box = tabla.find_all(class_="standard-box")

        counter = 0
        stats = {}
        group = ["Overall stats", "Opening stats", "Round stats", "Weapon stats"]
        
        for box in list_standard_box:
            stat_group = {}
            
            for row in box.find_all(class_="stats-row"):
                labels = [span.text for span in row.find_all('span')]
                stat_group[labels[0]] = labels[-1]

            stats[group[counter]] = stat_group
            counter += 1

        # Gracias ChatGPT, código para crear un DataFrame con subcolumnas
        df = pd.DataFrame(
            {
                (outer_key, inner_key): value 
                   for outer_key, inner_dict in stats.items() 
                   for inner_key, value in inner_dict.items()
            },
            index=[nickname]
        )
        
        return df
    
    def stats_players_team(self, team: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas individuales de cada integrante del
        equipo consultado.

        team: /id/nombre (e.g. /4608/natus-vincere)
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
            df = self.individual_stats(player)
            df_players = pd.concat([df_players, df])
            
        return df_players
    
    def teams_major_qualifier(self) -> list:
        """
        Retorna una lista de diccionarios con los grupos de los equipos de las clasificatorias
        del major, con el formato "Nombre_equipo": "/id/nombre"
        """
        ulr_qualifier = "https://www.hltv.org/major/qualifier"
        response = self.scraper.get(ulr_qualifier)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Error"

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

        return list_of_groups

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
            
    def pistol_rounds(self, side: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas anuales de los equipos para las
        rondas de pistolas.

        side: side ("both", "ct" "tt")
        """
        if side == "both":
            side_param = ""
        elif side == "ct":
            side_param = "&side=COUNTER_TERRORIST"
        elif side == "tt":
            side_param = "&side=TERRORIST"

        url_pistol_round = self.url_base + "/stats/teams/pistols" + self.params + side_param
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
    
    def team_stats_by_map(self, team: str, map_name: str) -> pd.DataFrame:
        """
        Retorna un DataFrame con las estadísticas del equipo en el mapa a analizar.
        team: /id/nombre (e.g. /4608/natus-vincere)
        pueden poner su dustdos como ejemplo xdxd
        """
        self.maps = map_name
        self.def_params(self.statDate, self.endDate, self.matchType, self.maps, self.rankingFilter)
        return self.stats_players_team(team)