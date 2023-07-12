from pprint import pprint
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


def make_request():
    print('Iniciando raspagem')

    # URL da página
    url = 'https://steamdb.info/sales/'
    headers = {
        'authority': 'steamdb.info',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'cf_chl_2=b271e6ba39e733b; cf_clearance=kYWJdCJxymYabuSboIpzO077cyLllvrPJhxi3UsHqgw-1689105666-0-160; __cf_bm=1p.FDypib9QrxlQ4yUFMTJER.Nse616HVD3hRXikYZs-1689108971-0-AdCUaiOD5rYw8ypF7Xc60nST6Uc1L2iz+WYG/VRm7x3O2Y0N/6+Yh9FmMbhZalxjUuO/O91M+SubrJ6VGsQBVjY=',
        'pragma': 'no-cache',
        'referer': 'https://steamdb.info/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
    
    response = requests.get(url, headers=headers)

    # Verifique se a requisição foi bem-sucedida
    if response.status_code == 200:
        print('RESP 200')
        soup = BeautifulSoup(response.content, 'html.parser')
        header_table = soup.find('tr', class_= 'text-left')
        body_table = soup.find_all(class_= 'app')

    else:
        print('A requisição não foi bem-sucedida.')

    # print(f" CABEÇALHO TABELA {header_table.text}")
    # print(f" LISTA DE ITENS {body_table}")
    name_game = []
    price_discount = []
    price = []
    rating = []
    end_in = []
    started = []
    realease = []

    for row in body_table:
        cells = row.find_all('td')
        
        for cell_name in cells:
            row_data = cell_name.find_all('a', class_='b')
            for item in row_data:
                row_text = item.text.strip()
                name_game.append(row_text)

        for cell_price_discount in cells:
            if 'price-discount-major' in cell_price_discount.get('class', []):
                cell_text = cell_price_discount.text.strip()
                price_discount.append(cell_text)

        for cell_price in cells:
            if cell_price.text.startswith('R$'):
                price_value = cell_price.text.split('R$')[1].strip()
                price.append(price_value)

        for cell_rating in cells:
            if 'price-discount-major' not in cell_rating.get('class', []) \
                and 'price-discount' not in cell_rating.get('class', []):

                if 'data-sort' in cell_rating.attrs and cell_rating.text.endswith('%'):
                    rating_value = cell_rating.text.split('%')[0]
                    # print(f"rating_value===={rating_value}")
                    rating.append(rating_value)
            
        
        # for cell_ends_in in cells:
        #     print(f"cell_ends_in {cell_ends_in}")
        #     if 'timeago' in cell_ends_in.get('class', []):
        #         cell_text = cell_ends_in.text.strip()
        #         end_in.append(cell_text)
        

        
   
    # print(f" NOME DO GAME {name_game}")
    # print(f" price_discount {price_discount}")
    print(f" rating {rating}")
    # print(f" end_in {end_in}")
                                 




    data_header_table = header_table.text
    # data_body_table = header_table.text

    # name_game     = body_table.find_all('a',attrs={'class':'b'})
    # release_date  = body_table.find_all('td', attrs={'td', {'class':'price-discount-major'}})
    # rating_score  = soup.find_all(class_='s-hit--score s-hit--score__good')
    # price_discount = soup.find_all('td', class_='price-discount-major')

    # list_games    = [ li.text for li in lineTable ]
   





























    # pprint(f" LISTA DE ITENS {dataInit}")
    # list_release_date = [ li.text for li in release_date ]
    # list_rating_score = [ li.text for li in rating_score ]
    # list_price        = [ li.text for li in price ]




    # chrome_options = Options()
    # chrome_options.add_argument(f'headers={headers}')
    # chrome_options.add_argument(f"--authority={headers['authority']}")
    # chrome_options.add_argument(f"--accept={headers['accept']}")
    # chrome_options.add_argument(f"--accept-language={headers['accept-language']}")
    # chrome_options.add_argument(f"--cache-control={headers['cache-control']}")
    # chrome_options.add_argument(f"--cookie={headers['cookie']}")
    # chrome_options.add_argument(f"--pragma'={headers['pragma']}")
    # chrome_options.add_argument(f"--referer'={headers['referer']}")
    # chrome_options.add_argument(f"--sec-ch-ua'={headers['Sec-Ch-Ua']}")
    # chrome_options.add_argument(f"--sec-ch-ua-mobile'={headers['sec-ch-ua-mobile']}")
    # chrome_options.add_argument(f"--sec-ch-ua-platform'={headers['sec-ch-ua-platform']}")
    # chrome_options.add_argument(f"--sec-fetch-dest'={headers['sec-fetch-dest']}")
    # chrome_options.add_argument(f"--sec-fetch-mode'={headers['sec-fetch-mode']}")
    # chrome_options.add_argument(f"--sec-fetch-site'={headers['sec-fetch-site']}")
    # chrome_options.add_argument(f"--sec-fetch-user'={headers['sec-fetch-user']}")
    # chrome_options.add_argument(f"--upgrade-insecure-requests'={headers['upgrade-insecure-requests']}")
    # chrome_options.add_argument(f"--user-agent'={headers['User-Agent']}")
    
 
    # # Configure os headers personalizados
    # for header, value in headers.items():
    #     print(f"--{header}={value}")
    #     chrome_options.add_argument(f"--{header}={value}")
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options=chrome_options)

    # print('Entrando no site...')
    # driver.get(url)

    # time.sleep(20)


    # print('Encontrando o elemento na página...')
    # element_table= '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[2]/table'
    # element_find = driver.find_element(By.XPATH, element_table)
    # html_content = element_find.get_attribute('outerHTML')
    # print(element_find)
    # print(html_content)
    # print(html_content)


    # print('Requisitando com BS4...')
    # response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    #     html_content = response.content
    # else:
    #     print('A solicitação não foi bem-sucedida. Código de status:', response.status_code)

    # soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup)


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

    # time.sleep(60)
    # driver.quit()

def make_req():
    # URL da página
    url = 'https://steamdb.info/sales/'

    header = {
            'authority: steamdb.info' \
            'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
            'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
            'cache-control: no-cache' \
            'cookie: cf_chl_2=b271e6ba39e733b; cf_clearance=kYWJdCJxymYabuSboIpzO077cyLllvrPJhxi3UsHqgw-1689105666-0-160; __cf_bm=1p.FDypib9QrxlQ4yUFMTJER.Nse616HVD3hRXikYZs-1689108971-0-AdCUaiOD5rYw8ypF7Xc60nST6Uc1L2iz+WYG/VRm7x3O2Y0N/6+Yh9FmMbhZalxjUuO/O91M+SubrJ6VGsQBVjY=' \
            'pragma: no-cache' \
            'referer: https://steamdb.info/' \
            'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
            'sec-ch-ua-mobile: ?0' \
            'sec-ch-ua-platform: "Linux"' \
            'sec-fetch-dest: document' \
            'sec-fetch-mode: navigate' \
            'sec-fetch-site: same-origin' \
            'sec-fetch-user: ?1' \
            'upgrade-insecure-requests: 1' \
            'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
            }
        # Cabeçalhos da requisição, caso não encontre, o site irá banir seu IP
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Cookie': 'cf_clearance=sIvqTUf6BFe5V_xONZu8SIPi2ZTukyyDbPY1HMAro5k-1688344842-0-160; __cf_bm=G7nU3oNoZfnaDe1L8N3J.f5fvREJdzm0x9_DuE0wznU-1688513997-0-AaxhlyiULh+y3TO90Y5TMNrzv6s69Mhe0Vkeh2nP/zEm/kS38+l7RnTZ1a5/STWkRlGz6EjzCP3dsygcEJnlsbbT2HcSI5w+XMBwaX4xJQf8',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    # Faz a requisição para a página com os cabeçalhos
    response = requests.get(url, headers=headers)

    # Obtém o conteúdo HTML da resposta
    html = response.content

    # Analisa o HTML usando o BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')


    game_items = soup.find_all('tr', class_='app')
        
    #game_items - Apenas para teste

    titulos = []
    precos = []
    #Extraindo o preço e o titulo dos games da pagina Sales
    elementos = soup.find_all('td', class_='applogo')
    for elemento in elementos:
        titulo_elemento = elemento.find_next('td').find('a', class_='b')
        if titulo_elemento:
            titulo = titulo_elemento.text.strip()
            titulos.append(titulo)

        preco_elemento = elemento.find_next('td').find_next('td').find_next('td')
        if preco_elemento:
            preco = preco_elemento.text.strip()
            precos.append(preco)

    #Preparando os dados para criar um DataFrame Pandas
    Dados = {'Título' : titulos,'Preço' : precos}

    #Criando o DataFrame
    df = pd.DataFrame(Dados)
    print(df)

make_request()
# make_req()