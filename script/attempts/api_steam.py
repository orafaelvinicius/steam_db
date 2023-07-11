from pprint import pprint
import requests
import json
import pandas as pd

with open('./data/key_secret.json') as file:
    data_json = json.load(file)

steam_key = data_json['KEY_STEAM_API']
cs_go = 730
Dungeon_Survivors = 2336730

class API_STEAM:
    def __init__(self):
        self.api_key = steam_key
        self.appid = cs_go
        self.df_init = pd.DataFrame()


    def get_all_games(self):
        '''
        Endpoint que retorn todos os jogos da plataforma e seus ids
        '''
        url = f"http://api.steampowered.com/ISteamApps/GetAppList/v2?key={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            games   = data['applist']['apps']
            # name    = games['name']
            # id      = games['appid']
            
            for game in games:
                print(game['appid'])
            
            df = pd.DataFrame(games)
            self.df_init = pd.concat([self.df_init, df])
            print(self.df_init)

            return df
        else:
            return None

    # if all_games is not None:
    #     for game in all_games:
    #         print()
    # else:
    #     print("Não foi possível obter a lista de jogos.")

    def get_detail(self):
        '''
        Requisições ao endpoint que fornece detalhes como:
        * Nome
        * Preço
        * Grátis (boolean)
        * Requisitos do pc
        dos jogos a partir de seus ids
        '''
        url = f"https://store.steampowered.com/api/appdetails/?appids={self.appid}"
        resp = requests.get(url)
        
        if resp.status_code == 200:
            data = resp.json()
            
            return pprint(data)
        else:
            return print("Falhou")

    def get_price(self):
        url = f"https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/?key={self.api_key}&appid={self.appid}"
        resp = requests.get(url)

        if resp.status_code == 200:
            data = resp.json()
            
            return pprint(data)
        else:
            return print("Falhou")

    
    def get_rating(self):
        pass

    def get_started(self):
        pass

    def get_realease(self):
        pass

    def get_discount_parcent(self):
        pass

    def run(self):
        print('api_key: ', self.api_key )
        print('steam_key: ', steam_key )

        self.get_all_games()
        # self.get_detail(cs_go)
        # self.get_price(self.api_key, cs_go)

if __name__ == '__main__':
    req = API_STEAM()
    req.run()


## TESTE DE FUNÇÃO
# def get_all_games():
#         '''
#         Endpoint que retorn todos os jogos da plataforma e seus ids
#         '''
#         url = f"http://api.steampowered.com/ISteamApps/GetAppList/v2?key={steam_key}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             games   = data['applist']['apps']
#             # name    = games['name']
#             # id      = games['appid']

#             for game in games:
#                 print(game['appid'])
            
#             df = pd.DataFrame(games)
#             print(df)

#             return games
#         else:
#             return None

# get_all_games()
# # if all_games is not None:
# #     for game in all_games:
# #         print(game['appid'])
# # else:
# #     print("Não foi possível obter a lista de jogos.")