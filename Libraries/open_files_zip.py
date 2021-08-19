import os
from pathlib import Path, PurePath
from zipfile import ZipFile
from datetime import datetime
import csv
# from Variables.config import ROOT, NOW, DOWNLOAD_DIRECTORY

ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
NOW = datetime.now().strftime("%d%m%Y%H%M")
DOWNLOAD_DIRECTORY = os.path.join(ROOT, "Downloads")


def read_files():
    print("*"*30)
    for diretory in os.listdir(DOWNLOAD_DIRECTORY):
        zip_file = os.path.join(DOWNLOAD_DIRECTORY, diretory)

        if zip_file.endswith('.zip'):
            with ZipFile(zip_file, "r") as myzip:
                file = myzip.namelist()[0]

                myzip.extractall(DOWNLOAD_DIRECTORY)
                # csv_file = os.path.splitext(file)[0]+".csv"

                # # print('*'*40, x)
                # with open(os.path.join(DOWNLOAD_DIRECTORY, diretory), "r+", encoding="utf-8") as csv:

                #     reader = csv.reader(csv, delimiter=';')

                #     for row in reader:
                #         print(row)


if __name__ == "__main__":
    read_files()
