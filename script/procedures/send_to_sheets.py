import json
import os.path
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Definindo scopo, id e celulas da planilha
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID = '1b9ifiE_Vg4d8sqxmvFRpXj6h2VLjHhwcIFIwVRtNCgc'
SAMPLE_RANGE_NAME = 'Folha1!A1:Z'

def data_to_sheets():
    """
    Função responsável por acessar o Google Sheets e escrever os dados na planilha
    """
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    print('Credenciando...')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './data/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        print('Criando instânciada planilha')
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        print('Lendo arquivo')
        with open('split_lista_steam.json') as file:
            json_data = json.load(file)
        
        data = [json_data["columns"]] + json_data["data"]
        
        print('Carregando dados')
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,
                                    valueInputOption="USER_ENTERED",
                                    body={"values": data}).execute()
        
        print("Carregamento concluído com sucesso!")

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    data_to_sheets()
