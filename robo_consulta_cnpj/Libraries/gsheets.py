from robot.api import logger
from pathlib import Path, PurePath
from oauth2client.service_account import ServiceAccountCredentials
from gspread_pandas import Client, Spread
from Variables import config


def create_gsecret_json(gsecret_json_path, gsecret):
    secret_file_path = Path(gsecret_json_path)
    if not secret_file_path.is_file():
        logger.info('json com id e secret da aplicação não encontrado. Criando'
                    ' no local: {gsecret_json_path}.')
        secret_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(secret_file_path, 'w') as secrets_json:
            secrets_json.write(gsecret)
        logger.info('Arquivo criado.')


def setup_gsheets():

    creds_folder = config.SHEETS_CREDS_PPATH
    secrets_folder = \
        config.GOOGLE_SECRET_JSON_PPATH
    GOOGLE_SECRET = config.GOOGLE_SECRET
    create_gsecret_json(secrets_folder, GOOGLE_SECRET)
    creds_file = Path(PurePath(creds_folder, "default"))
    if not creds_file.is_file():
        creds_file.parent.mkdir(parents=True, exist_ok=True)
        G_CREDS = config.G_CREDS
        try:
            with open(creds_file, 'w') as default_file:
                default_file.write(G_CREDS)
        except Exception as e:
            logger.error(
                f"Erro ao configurar as credenciais do Google Sheets\n {e}")
            config.use_gsheets = False


def get_gspreadsheet_by_id(spreadsheet_id, **kwargs):
    client = Client()
    return Spread(spreadsheet_id, client=client, **kwargs)


def upload_dataframe_gsheets(dataframe, gsheets_id, sheet_name, **kwargs):
    gspreadsheet = get_gspreadsheet_by_id(gsheets_id, sheet=sheet_name,
                                          **kwargs)
    gspreadsheet.df_to_sheet(dataframe, index=False, sheet=sheet_name,
                             replace=True)
