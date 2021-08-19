from pathlib import Path, PurePath
import os
from datetime import datetime

AREA_NAME = 'consulta_cnpj_rf'


# ==================== CHROME ==========================
URL = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"

BROWSER_DIRECTORY = "C:\\browsers\\Chrome\\89\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"
CHROMEDRIVER_DIRECTORY = "C:\\browsers\\Chrome\\89\\chromedriver.exe"
# ======================================================


# =================== Timeout Robot ====================
DEFAULT_SELENIUM_TIMEOUT = '40 seconds'
DEFAULT_DOWNLOAD_TIMEOUT = '60 seconds'
# ======================================================


# ====================== DIRETÓRIOS LOCAIS ======================
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
NOW = datetime.now().strftime("%d%m%Y%H%M")
DOWNLOAD_DIRECTORY = os.path.join(ROOT, "Downloads")
# ===============================================================


# ====================== Mongo ======================
MONGO_ADDR = "localhost",
MONGO_COMMONS_DB = "commons",
MONGO_PORT = "27017",
MONGO_PWD = "admin",
MONGO_URI = "mongodb://localhost:27017/?authSource=admin",
MONGO_USER = "root",
MONGO_USER_CONFIG_COLLECTION = "user-configurations"
# ===================================================

