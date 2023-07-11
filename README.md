# Desafio técnico beAnalytic

Este desafio foi idealizado pela beAnalytic para realização do processo seletivo para o cargo de engenheiro de dados júnior.

## Desafio:

Realizar a extração das informações que conseguir da base de dados listada no website: https://steamdb.info/sales/ , armazenar estes dados no Google BigQuery e em seguida exporte ou conecte esses dados em um Google Sheets.

## Problemas encontrados:

A plataforma steamdb conta com camadas de proteção contra raspagem dos seus dados, a própria plataforma deixa explícito que não apoia este tipo de prática. Para contornar este problema, utilizei algumas abordagens como:
_ Alteração do cabeçalho das requisições para passar pela proteção
_ lib oficial da Steam
_ API oficial da Steam (recomendado pela plataforma steamdb)
_ Raspagem através do endpoint secundário (/instantsearch/) fornecido pela plataforma

### Resumo da abordagem escolhida

A abordagem escolhida foi a raspagem dos dados acessando através do endpoint secundário (retirado do endpoint robot.txt) para se aproximar ao máximo do que foi pedido no desafio a partir dos seguintes passos:

1. Acessar o site utilizando Selenium com as devidas configurações de navegador
2. Capturar o HTML da página utilizando BeautifulSoup
3. Realizar o tratamento do HTML recebido
4. Criar um dataframe com Pandas
5. Realizar o tratamento dos dados com Pandas
6. Exportar os dados para uma planilha no Google Sheets
7. Enviar os dados para o BigQuery

### Requisitos:

Para executar a aplicação, você precisa do arquivo com credenciais para acessar o Google Sheets e BigQuery, e também ter o Docker instalado.

## Execução:

Para executar a aplicação, você pode:
Acessar a pasta "script" e executar o comando
`python3 main.py`
ou executar o comando:
`docker build -t scraping-app .`
`docker run -d scraping-app`
