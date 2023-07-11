import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import json


def data_to_bigQuery():
    print('Iniciando bigquery')
    dataset_id = 'tabela_de_jogos'
    table_name = 'lista_de_jogos'
    KEYS = service_account.Credentials.from_service_account_file("./data/service_account.json")
    
    print('Cria a instância do bigQuery') 
    client = bigquery.Client(credentials=KEYS)

    table_ref = f"{KEYS.project_id}.{dataset_id}.{table_name}2"
    print(f'TABELA DE REFERENCIA === {table_ref}') 

    print('Lendo arquivo')
    df_excel = pd.read_excel('./lista_steam.xlsx', 'Sheet1')
    # df_json = pd.read_json('./split_lista_steam.json')

    print('Carregando tabela...') 
    job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name_game","STRING"),
        bigquery.SchemaField("release_date","DATE"),
        bigquery.SchemaField("rating_score","FLOAT"),
        bigquery.SchemaField("price","FLOAT")
    ]
    )

    print('Carregando dados...') 
    job = client.load_table_from_dataframe(df_excel, table_ref, job_config=job_config)
    job.result()

    if job.errors:
        for error in job.errors:
            print(f"Erro de carregamento: {error['message']}")
    else:
        print("Carregamento concluído com sucesso!")
    
    # print('Enviando dados com pandas to_gbq') 
    # df_excel.to_gbq(table_ref, project_id=KEYS.project_id, if_exists='replace')    




if __name__ == '__main__':
    data_to_bigQuery()

