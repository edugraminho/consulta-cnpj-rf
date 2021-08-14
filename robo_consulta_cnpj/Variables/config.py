from pathlib import Path, PurePath
import os
import logging
from datetime import datetime
from Libraries import hvclient

AREA_NAME = 'consulta_cnpj_rf'

############ CHROME ###############################
CHROME_VERSION = 89
BROWSER_DIRECTORY = os.environ.get('CHROME').format(CHROME_VERSION)
CHROMEDRIVER_DIRECTORY = os.environ.get('CHROMEDRIVER').format(CHROME_VERSION)

URL = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"


############ Timeout ###############################
DEFAULT_SELENIUM_TIMEOUT = '40 seconds'
DEFAULT_DOWNLOAD_TIMEOUT = '60 seconds'

############ DIRETÓRIOS LOCAIS ###############################
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
now = datetime.now().strftime("%d%m%Y%H%M")

DOWNLOAD_DIRECTORY = os.path.join(ROOT, "Downloads")

############ Mongo ###############################
DB_CREDENTIALS = hvclient.get_credentials('mongo')
MONGO_USER = DB_CREDENTIALS.get('USER')
MONGO_PWD = DB_CREDENTIALS.get('PWD')
MONGO_URI = DB_CREDENTIALS.get('URI')

############ Logger ###############################
default_log_msg = "[{ticket_id}] - [{prestador}] - [{nr}] {msg}"
out_robot_log_level = logging.INFO
out_robot_file_log_level = logging.INFO
out_robot_logger_name = 'consumidor-top-saude'
out_robot_log_format = f"%(asctime)s - [%(levelname)s] - %(message)s"
log_path = Path(PurePath(ROOT, 'Results'))
if not log_path.is_dir():
    log_path.mkdir(parents=True, exist_ok=True)


# # ---------------------- GSHEETS -----------------------------
# use_gsheets = True
# GSHEETS_ID = CREDENTIALS.get('GSHEET_ID')
# GSHEET_NAME = 'robo02'
# ATENCAO_OPERACIONAL_SHEET_NAME = 'Atenção Operacional'
# GSUITE_CREDENTIALS = hvclient.get_credentials('gsuite')
# GOOGLE_SECRET = GSUITE_CREDENTIALS.get('GOOGLE_SECRET')
# G_CREDS = GSUITE_CREDENTIALS.get("GOOGLE_CREDENTIALS")

# os.environ['GSPREAD_PANDAS_CONFIG_DIR'] = ROOT.as_posix()
# GOOGLE_SECRET_JSON_PPATH = fr'{ROOT}\google_secret.json'
# SHEETS_CREDS_PPATH = fr'{ROOT}\creds'
# atencao_operacional = []
