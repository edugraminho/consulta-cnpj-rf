import xlsxwriter

class XLSX_dataBase:
    workbook = None
    worksheet = None

    def __init__(self, fileName):
        self.workbook = xlsxwriter.Workbook(fileName)
        self.worksheet = self.workbook.add_worksheet("CNPJ")

    def write(self, content_list):
        column_Name_list = []
        if len(content_list) > 0:
            row = 0
            for item in content_list:
                if row == 0:
                    column = 0
                    for key in item:
                        column_Name_list.append(key)
                        self.worksheet.write(row, column, key)
                        column += 1
                column = 0
                row += 1
                for column_Name in column_Name_list:
                    self.worksheet.write(row, column, item[column_Name])
                    column += 1



    def close(self):
        self.workbook.close()

