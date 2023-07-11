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


# Cabeçalhos da requisição para passar pelo captcha



def make_request():
    print('Iniciando raspagem')
    # while num_page < 25: 
    #     num_page += 1

    # print(f'Fazendo a requisição na página {num_page} de 25')

    # URL da página
    url = 'https://steamdb.info/sales/'
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control":"no-cache",
        "Cookie":"cf_clearance=vT10Zq8uHaeH8MmMNhGHFP4LQ6iv.hfSwphR0GQae0Q-1688407048-0-160; __cf_bm=oGC5WUbjDqY71so0jnpdYgRt53kX9mLkeYhMSj5IbXQ-1688997364-0-AV5ic3789+iYLquayGk/7uflQexLqDmeN+hbLCF6f1kAdj4bl4DMndNnfJ34PmnB1alPGIYAsiTf0Q0oyV6b9mE=",
        "Pragma":"no-cache",
        "Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "Sec-Ch-Ua-Mobile":"?0",
        "Sec-Ch-Ua-Platform":"Linux",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"none",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }


    # print('Configurando navegador...')
    # chrome_options = Options()
    # chrome_options.add_argument(f'header={headers}')
    # # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options=chrome_options)

    # print('Entrando no site...')
    # driver.get(url)
    # time.sleep(3)

    print('Requisitando com BS4...')
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.content
    else:
        print('A solicitação não foi bem-sucedida. Código de status:', response.status_code)

    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)

    # print('Encontrando o elemento na página...')
    # element_table= '/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/ol'
    # element_find = driver.find_element(By.XPATH, element_table)
    # html_content = element_find.get_attribute('outerHTML')
    # print(element_find)
    # print(html_content)
    # print(html_content)

    # print('Paerceando pelo HTML para encontrar os campos necessários')
    # soup = BeautifulSoup(html_content, "html.parser")
    # print(soup)


    # list_all_data = soup.find_all(class_='ais-Hits-list')
    # list_item     = soup.find_all(class_='ais-Hits-item')
    # name_game     = soup.find_all(class_='ais-Highlight-nonHighlighted')
    # release_date  = soup.find_all(class_='s-hit--release')
    # rating_score  = soup.find_all(class_='s-hit--score s-hit--score__good')
    # price         = soup.find_all(class_='s-hit--price')

    # list_name_game    = [ li.text for li in name_game ]
    # list_release_date = [ li.text for li in release_date ]
    # list_rating_score = [ li.text for li in rating_score ]
    # list_price        = [ li.text for li in price ]

    # list_name_game.extend(list_name_game)
    # list_release_date.extend(list_release_date)
    # list_rating_score.extend(list_rating_score)
    # list_price.extend(list_price)

    # print('Criando objetos do dataframe')
    # data_name_game    = {'name_game'   : list_name_game}
    # data_release_date = {'release_date': list_release_date}
    # data_rating_score = {'rating_score': list_rating_score}
    # data_price        = {'price'       : list_price}
    
    # # print('Criando tipagem dos dados')
    # dtype_name_game    = {'name_game'   : str}
    # dtype_release_date = {'release_date': str}
    # dtype_rating_score = {'rating_score': str}
    # dtype_price        = {'price'       : str}

    # print('Criando dataframes')
    # # df_name_game    = pd.DataFrame(data_name_game,    dtype = dtype_name_game)
    # # df_release      = pd.DataFrame(data_release_date, dtype = dtype_release_date)
    # # df_rating_score = pd.DataFrame(data_rating_score, dtype = dtype_rating_score)
    # # df_price        = pd.DataFrame(data_price,        dtype = dtype_price)
    # df_name_game    = pd.DataFrame(data_name_game)
    # df_release      = pd.DataFrame(data_release_date)
    # df_rating_score = pd.DataFrame(data_rating_score)
    # df_price        = pd.DataFrame(data_price)
    
    # print('Concatenando Dataframes')
    # df_init = pd.concat([df_name_game, df_release, df_rating_score, df_price], axis=1)
    # print(df_init)

    # if num_page > 26:
    #     driver.quit()

    time.sleep(30)
    # driver.quit()

make_request()