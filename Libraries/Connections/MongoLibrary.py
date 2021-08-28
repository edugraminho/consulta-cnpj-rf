from Variables.config import *
from mongoengine import connect, disconnect
from robot.api import logger
      
class MongoLibrary:

    def __init__(self):
        self.alias = AREA_NAME
        self.db = AREA_NAME
        self.username = MONGO_USER
        self.password = MONGO_PWD
        self.host = MONGO_URI

    def open_connections(self):
        try: 
            logger.info(f'Conectando no Banco de Dados', also_console=True)
            connect(
                alias = self.alias,
                db = self.db,
                username = self.username,
                password = self.password,
                host = self.host
            )
        except:
            logger.info(f'ERRO Conectando no Banco de Dados', also_console=True)


    def close_connections(self):
        disconnect(alias = self.alias)

