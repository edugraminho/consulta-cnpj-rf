from Database.models import Empresas
from Variables.config import *
from robot.api import logger



class InsertItems():
    def insert_csv_into_db(self, reader):

        try:
            empresas = [Empresas(**
                                {
                                    "cnpj_basico": int(data[0]) if data[0] != '' else -1,
                                    "razao_social": str(data[1]),
                                    "natureza_juridica":data[2],
                                    "qualificacao_do_responsavel": data[3],
                                    "capital_social_da_empresa": data[4].replace(",", ""),
                                    "porte_da_empresa": data[5]
                                }) for  data in reader]
            logger.info(f'Inserindo empresas no banco de dados', also_console=True)
            logger.info(len(empresas), also_console=True)


            Empresas.objects.insert(empresas, load_bulk=False)

        except Exception as e:
            logger.info(f'Erro: {e}', also_console=True)