from __future__ import print_function
import os.path
import math
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Se necessário, instale as bibliotecas com: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Se necessário, forneça as credenciais corretas do Google Sheets

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet
SAMPLE_SPREADSHEET_ID = '1_vxRwC70k3OMeHC0H1mlOkAr3BtDBN19Y6LY0J15um8'
SAMPLE_RANGE_NAME = 'engenharia_de_software!C4:F27'

def calcular_situacao(media, faltas, total_aulas):
    if faltas > 0.25 * total_aulas:
        return "Reprovado por Falta", 0
    elif media < 5:
        return "Reprovado por Nota", 0
    elif 5 <= media < 7:
        naf = max(0, math.ceil(10 - media))
        return "Exame Final", naf
    else:
        return "Aprovado", 0

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    # Call the Sheets API
    # Ler informações do Google Sheets

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    total_aulas = 60  # Defina o número total de aulas aqui

    for i in range(len(values)):  # Começar do índice 0 para ignorar o cabeçalho
        row = values[i]

        faltas = int(row[0])
        p1 = float(row[1]) 
        p2 = float(row[2]) 
        p3 = float(row[3]) 

        media = math.ceil((p1 + p2 + p3) /  30)  # Dividir por 30 para ajustar a escala e arredonda para o próximo número inteiro

        situacao, naf = calcular_situacao(media, faltas, total_aulas)


        # Atualizar os valores no Google Sheets
        update_values = [
            [faltas, p1, p2, p3, situacao, naf]
        ]
        update_range = f'engenharia_de_software!C{i + 4}:H{i + 4}'  # +4 para compensar o cabeçalho e índice 1
        update_body = {'values': update_values}

        sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=update_range,
            body=update_body,
            valueInputOption="RAW"
        ).execute()

        print(f"Aluno na linha {i + 4}: Situação atualizada para {situacao} (NAF: {naf})")

if __name__ == '__main__':
    main()


    