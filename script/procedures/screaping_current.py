# RASPE TODOS OS DADOS DO SITE 
# Ordene os dados
# Formate as datas e preços
# coloca num parquet só pra ficar bonito
# COLOQUE EM UMA PLANILHA NO BigQuery
# COLOQUE EM UMA PLANILHA NO GOOGLE SHEETS
# Roda com docker
# Crie também um arquivo parquet e mostre e explique o porque
# https://steamdb.info/sales/

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import json



# with open("/home/beanalytic/beanalytic_case/data/key_secret.json") as file:
#     data_json = json.load(file)
# KEY_ANTI_CAPTCHA = data_json['KEY_ANTI_CAPTCHA']

### Abordagem com Selenium
# # Instalando a versão compatível do Chrome
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Steamdb:
    def __init__(self):
        self.num_page          = 0
        self.list_name_game    = []
        self.list_release_date = []
        self.list_rating_score = []
        self.list_price        = []
        self.df_init           = pd.DataFrame()
        self.df_name_game      = pd.DataFrame()
        self.df_release        = pd.DataFrame()
        self.df_rating_score   = pd.DataFrame()
        self.df_price          = pd.DataFrame()
        
    def make_request(self):
        print('Iniciando raspagem')
        while self.num_page < 2: 
            self.num_page += 1

            print(f'Fazendo a requisição na página {self.num_page} de 25')

            url = f'https://steamdb.info/instantsearch/?page={self.num_page}'

            print('Configurando navegador...')
            chrome_options = Options()
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
            chrome_options.add_argument(f'user-agent={user_agent}')
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)

            print('Entrando no site...')
            driver.get(url)
            time.sleep(3)

            print('Encontrando o elemento na página...')
            element_table= '/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/ol'
            element_find = driver.find_element(By.XPATH, element_table)
            html_content = element_find.get_attribute('outerHTML')
            print(element_find)
            print(html_content)
            print(html_content)

            print('Paerceando pelo HTML para encontrar os campos necessários')
            soup = BeautifulSoup(html_content, "html.parser")
            print(soup)

            list_all_data = soup.find_all(class_='ais-Hits-list')
            list_item     = soup.find_all(class_='ais-Hits-item')
            name_game     = soup.find_all(class_='ais-Highlight-nonHighlighted')
            release_date  = soup.find_all(class_='s-hit--release')
            rating_score  = soup.find_all(class_='s-hit--score s-hit--score__good')
            price         = soup.find_all(class_='s-hit--price')

            list_name_game    = [ li.text for li in name_game ]
            list_release_date = [ li.text for li in release_date ]
            list_rating_score = [ li.text for li in rating_score ]
            list_price        = [ li.text for li in price ]

            self.list_name_game.extend(list_name_game)
            self.list_release_date.extend(list_release_date)
            self.list_rating_score.extend(list_rating_score)
            self.list_price.extend(list_price)

            print('Criando objetos do dataframe')
            data_name_game    = {'name_game'   : self.list_name_game}
            data_release_date = {'release_date': self.list_release_date}
            data_rating_score = {'rating_score': self.list_rating_score}
            data_price        = {'price'       : self.list_price}
            
            # print('Criando tipagem dos dados')
            dtype_name_game    = {'name_game'   : str}
            dtype_release_date = {'release_date': str}
            dtype_rating_score = {'rating_score': str}
            dtype_price        = {'price'       : str}

            print('Criando dataframes')
            # self.df_name_game    = pd.DataFrame(data_name_game,    dtype = dtype_name_game)
            # self.df_release      = pd.DataFrame(data_release_date, dtype = dtype_release_date)
            # self.df_rating_score = pd.DataFrame(data_rating_score, dtype = dtype_rating_score)
            # self.df_price        = pd.DataFrame(data_price,        dtype = dtype_price)
            self.df_name_game    = pd.DataFrame(data_name_game)
            self.df_release      = pd.DataFrame(data_release_date)
            self.df_rating_score = pd.DataFrame(data_rating_score)
            self.df_price        = pd.DataFrame(data_price)
            
            print('Concatenando Dataframes')
            self.df_init = pd.concat([self.df_name_game, self.df_release, self.df_rating_score, self.df_price], axis=1)
            print(self.df_init)

            if self.num_page > 26:
                driver.quit()

    def export_to_excel(self, filename):
        print(self.df_init)
        print('Criando arquivo excel...')
        self.df_init.to_excel(filename, index=False)
        
    def export_to_json(self, filename):
        print('Criando arquivo json...')
        self.df_init.to_json(filename,orient="index")
        self.df_init.to_json(f'split_{filename}',orient="split") 

    def export_to_parquet(self, filename):
        print('Criando arquivo json...')
        self.df_init.to_parquet(filename)

    def run(self):
        self.make_request()
        self.export_to_excel('lista_steam.xlsx')
        self.export_to_json('lista_steam.json')
        self.export_to_parquet('lista_steam.parquet')
        return self.df_init

    

if __name__ == '__main__':
    steam = Steamdb()
    steam_return = steam.run()
    # print(steam_return)






