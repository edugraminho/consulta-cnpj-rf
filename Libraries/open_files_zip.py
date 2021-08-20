import os
from pathlib import Path, PurePath
from zipfile import ZipFile
from datetime import datetime
import csv
# from Variables.config import ROOT, NOW, DOWNLOAD_DIRECTORY


#TIRAR
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
NOW = datetime.now().strftime("%d%m%Y%H%M")
DOWNLOAD_DIRECTORY = os.path.join(ROOT, "Downloads")



def extract_csv_from_zip():
    print("*"*30)
    for diretory in os.listdir(DOWNLOAD_DIRECTORY):
        zip_file = os.path.join(DOWNLOAD_DIRECTORY, diretory)

        if zip_file.endswith('.zip'):
            with ZipFile(zip_file, "r") as myzip:
                myzip.extractall(DOWNLOAD_DIRECTORY)



def convert_to_csv():
    for file in os.listdir(DOWNLOAD_DIRECTORY):
        path_file = os.path.join(DOWNLOAD_DIRECTORY, file)

        if file.endswith('.EMPRECSV'):
            base = os.path.splitext(file)[0]
            path_base = os.path.join(DOWNLOAD_DIRECTORY, base)
            if base+".csv":
                print("Arquivo CSV já Existe")
            else:
                os.rename(path_file, path_base+".csv")



def read_csv():

    for csv_file in os.listdir(DOWNLOAD_DIRECTORY):

        if csv_file.endswith('.csv'):
            with open(os.path.join(DOWNLOAD_DIRECTORY, csv_file), "r+", encoding="utf-8") as csv_f:
                reader = csv.DictReader(csv_f, delimiter=';')
                for row in reader:
                    print(row)




if __name__ == "__main__":
    extract_csv_from_zip()
    convert_to_csv()
    read_csv()