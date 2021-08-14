import sqlite3
from sqlite3 import Error


class SQLite_dataBase:

    db = None
    progress = 0

    def __init__(self):

        self.db = sqlite3.connect(
            r"C:\\Users\\Prime\\projetos\\consulta_cnpj_rf\\database")

    def search(self, dict_param):
        # lendo os dados
        lista_dict = []
        cursor = self.db.cursor()

        cursor.execute(
            "select emp.situacao, cn.cnae, emp.cnpj, emp.razao_social, emp.nome_fantasia, emp.logradouro, emp.numero, emp.complemento, emp.bairro, emp.cep, emp.municipio, emp.uf, emp.ddd_1, emp.telefone_1, emp.email from cnaes_secundarios cn "
            "inner JOIN(SELECT situacao,cnpj,razao_social,nome_fantasia,logradouro,numero,complemento,bairro,cep,municipio,uf,ddd_1,telefone_1,email from empresas where razao_social like "
            "'%" + dict_param['razao_social'] + "%' and cnpj like '%" + dict_param['cnpj'] +
            "%' and situacao like '%" +
            dict_param['active_cnpj'] + "%' and nome_fantasia like "
            "'%" + dict_param['nome_fantasia'] +
            "%' and uf like '%" + dict_param['uf'] + "%')emp on "
            "cn.cnpj == emp.cnpj where cn.cnae like '%" + dict_param['cnae'] + "%'")

        # cursor.execute("select cn.cnae, emp.cnpj, emp.razao_social, emp.nome_fantasia, emp.uf from cnaes_secundarios cn "
        #                "inner JOIN(SELECT cnpj,razao_social,nome_fantasia,uf from empresas where razao_social like "
        #                "'%"+dict_param['razao_social']+"%' and cnpj like '%"+dict_param['cnpj']+"%' and nome_fantasia like "
        #                 "'%"+dict_param['nome_fantasia']+"%' and uf like '%"+dict_param['uf']+"%')emp on "
        #                 "cn.cnpj == emp.cnpj where cn.cnae like '%"+dict_param['cnae']+"%'")

        dataBase_List = cursor.fetchall()

        print("Consulta feita")
        print(len(dataBase_List))
        self.progress = 0
        count = 0
        for linha in dataBase_List:
            dict_result = {}
            dict_result['situacao'] = linha[0]
            dict_result['cnae'] = linha[1]
            dict_result['cnpj'] = linha[2]
            dict_result['razao_social'] = linha[3]
            dict_result['nome_fantasia'] = linha[4]
            dict_result['logradouro'] = linha[5]
            dict_result['numero'] = linha[6]
            dict_result['complemento'] = linha[7]
            dict_result['bairro'] = linha[8]
            dict_result['cep'] = linha[9]
            dict_result['municipio'] = linha[10]
            dict_result['uf'] = linha[11]
            dict_result['telefone'] = linha[12] + '-' + linha[13]
            dict_result['email'] = linha[14]
            lista_dict.append(dict_result)
            count += 1
            self.progress = int(count/len(dataBase_List)*100)

        self.db.close()

        return lista_dict

    def get_progress(self):
        return self.progress
