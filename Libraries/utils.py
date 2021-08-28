import os
import csv
from zipfile import ZipFile
from robot.api import logger

from Database.queries import InsertItems
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

def convert_to_csv():

    for file in os.listdir(DOWNLOAD_DIRECTORY):
        path_file = os.path.join(DOWNLOAD_DIRECTORY, file)

        if file.endswith('.EMPRECSV') or file.endswith('.SOCIOCSV') or file.endswith('.ESTABELE')or file.endswith('.CNAECSV'):
            base = os.path.splitext(file)[0]
            # path_base = os.path.join(DOWNLOAD_DIRECTORY, base)
            if base+".csv" in os.listdir(DOWNLOAD_DIRECTORY):
                logger.info(f'Este arquivo já existe', also_console=True)
                
            else:
                logger.info(f'Arquivo descompactado com Sucesso', also_console=True)
                os.rename(path_file, path_file+".csv")
                


def ler_csv():

    convert_to_csv()
    
    for csv_file in os.listdir(DOWNLOAD_DIRECTORY):

        if csv_file.endswith('.csv'):
            try:
                with open(os.path.join(DOWNLOAD_DIRECTORY, csv_file), "r", newline='') as csv_f:
                    reader = csv.reader(csv_f, delimiter=';')
                    return reader
            except Exception as e:
                logger.error(f'Erro ao ler o Csv: {e}')
                return False

        

def inserir_dados_no_bd(reader):
    

    InsertItems.insert_csv_into_db(reader)



