import os
import csv
from zipfile import ZipFile
from robot.api import logger

from Database.queries import *
from Variables.config import *

def extrair_csv_do_arquivo_zip():
    try:
        for diretory in os.listdir(DOWNLOAD_DIRECTORY):
            zip_file = os.path.join(DOWNLOAD_DIRECTORY, diretory)

            if zip_file.endswith('.zip'):
                logger.info(f'Extraindo o arquivo: {zip_file}', also_console=True)
                with ZipFile(zip_file, "r") as myzip:
                    myzip.extractall(DOWNLOAD_DIRECTORY)
        return True
    except Exception as e:
        logger.error(f'Erro ao extrair Csv: {e}')
        return False

def convert_to_csv(name):

    file_name = name.replace(" ", "_").lower()
    for file in os.listdir(DOWNLOAD_DIRECTORY):
        path_file = os.path.join(DOWNLOAD_DIRECTORY, file)

        if file.endswith('.EMPRECSV'):
            # base = os.path.splitext(file)[0]+".csv"
            # logger.info(f'************************{base}*****', also_console=True)

            # # path_base = os.path.join(DOWNLOAD_DIRECTORY, base)
            # if file in os.listdir(DOWNLOAD_DIRECTORY):
            #     logger.info(f'Este arquivo já existe', also_console=True)
            # else:
            logger.info(f'Arquivo descompactado com Sucesso', also_console=True)
            os.rename(path_file, os.path.join(DOWNLOAD_DIRECTORY, f"empresas_{file_name}_{NOW}.csv"))


        elif file.endswith('.SOCIOCSV'):
            # base = os.path.splitext(file)[0]+".csv"
            # path_base = os.path.join(DOWNLOAD_DIRECTORY, base)
            # if file in os.listdir(DOWNLOAD_DIRECTORY):
            #     logger.info(f'Este arquivo já existe', also_console=True)
            # else:
            logger.info(f'Arquivo descompactado com Sucesso', also_console=True)
            os.rename(path_file, os.path.join(DOWNLOAD_DIRECTORY, f"socios_{file_name}_{NOW}.csv"))   



        elif file.endswith('.ESTABELE'):
            # base = os.path.splitext(file)[0]+".csv"
            # path_base = os.path.join(DOWNLOAD_DIRECTORY, base)
            # if file in os.listdir(DOWNLOAD_DIRECTORY):
            #     logger.info(f'Este arquivo já existe', also_console=True)
            # else:
            logger.info(f'Arquivo descompactado com Sucesso', also_console=True)
            os.rename(path_file, os.path.join(DOWNLOAD_DIRECTORY, f"eslabelecimentos_{file_name}_{NOW}.csv"))
                


def inserir_dados_no_bd():
    
    for csv_file in os.listdir(DOWNLOAD_DIRECTORY):

        if csv_file.endswith('.csv'):
            try:
                with open(os.path.join(DOWNLOAD_DIRECTORY, csv_file), "r", newline='') as csv_f:
                    logger.info(f'Iniciando a Leitura e Insercao no BD do Arquivo: {csv_file}', also_console=True)

                    reader = csv.reader(csv_f, delimiter=';')
                    base = os.path.splitext(csv_file)[0].split("_")

                    if base[0] == "empresas":
                        inserir_empresas(reader)
                    if base[0] == "socios":
                        inserir_socios(reader)                    
                    if base[0] == "eslabelecimentos":
                        inserir_estabelecimentos(reader)

            except Exception as e:
                logger.error(f'Erro ao ler o Csv: {e}')
                return False

        

