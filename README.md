# ETL SteamDB

Esta aplicação tem o objetivo de realizar a extração, tratamento e carregamento do dados da página SteamDB que contém diversas informações sobre os jogos existentes na plataforma steam com preço, promoções, descontos entre outros.

## Desafio:

Realizar a extração das informações que conseguir da base de dados listada no website: https://steamdb.info/sales/ , armazenar estes dados no Google BigQuery e em seguida exporte ou conecte esses dados em um Google Sheets.

## Problemas encontrados:

A plataforma steamdb conta com camadas de proteção contra raspagem dos seus dados, a própria plataforma deixa explícito que não apoia este tipo de prática.

Para contornar este problema, utilizei algumas abordagens como:

- Alteração do cabeçalho das requisições para passar pela proteção
- lib oficial da Steam
- API oficial da Steam (recomendado pela plataforma steamdb)
- Raspagem através do endpoint secundário (/instantsearch/) fornecido pela plataforma

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

Além do ambiente configurado e/ou também ter o Docker instalado, para executar a aplicação, você precisa do arquivo com credenciais para acessar o Google Sheets e BigQuery. Estas credenciais serão obtidas através de uma [conta de serviços do Google](https://support.google.com/a/answer/7378726?hl=pt-BR)

## Execução:

Para executar a aplicação, você pode:
executar os comandos [Linux Ubuntu 20]

```sh
python3 -M venv venv
pip install -r requirements.txt
source venv/bin/activate
cd script
python3 main.py
```

ou executar os comandos:

```sh
docker build -t scraping-app .
docker run -d scraping-app
```

## Arquitetura

```
├── data
│   ├── client_secret.json
│   ├── exemple_client_secret.json
│   ├── exemple_service_account.json
│   ├── key_secret.json
│   └── service_account.json
├── Dockerfile
├── requirements.txt
└── script
    ├── attempts
    │   ├── api_steam.py
    │   ├── force_antiCAPTCHA.py
    │   ├── lib_steam.py
    │   └── req_sales.py
    ├── main.py
    ├── procedures
    │   ├── screaping.py
    │   ├── send_to_big_query.py
    │   └── send_to_sheets.py
    └── token.json
```

### Descrição dos diretórios e arquivos

- scripts
  - attempts: Diretório responsável por armazenar todas as tentativas de realizar a tarefa
  - procedures: Diretório responsável por armazenar todos os executores do main.py
- data: Armazenar arquivos de credenciais

- Dockerfile: Executor do docker
- requirements.txt: Requerimentos da aplicação

### links úteis:

[steamdb](https://steamdb.info/sales/)
[steamdb robots](https://steamdb.info/robots.txt)
[API Steam](https://partner.steamgames.com/doc/webapi/ISteamApps)
