from Database.models import Empresas, Estabelecimentos, Socios
from Variables.config import *
from robot.api import logger


def inserir_empresas(reader):

    try:
        empresas = [Empresas(**
                             {
                                 "cnpj_basico": int(data[0]) if data[0] != '' else -1,
                                 "razao_social": str(data[1]),
                                 "natureza_juridica":data[2],
                                 "qualificacao_do_responsavel": data[3],
                                 "capital_social_da_empresa": data[4].replace(",", ""),
                                 "porte_da_empresa": data[5]
                             }) for data in reader]
        logger.info(f'Inserindo empresas no banco de dados',
                    also_console=True)
        logger.info(len(empresas), also_console=True)

        Empresas.objects.insert(empresas, load_bulk=False)

    except Exception as e:
        logger.info(f'Erro: {e}', also_console=True)


def inserir_estabelecimentos(reader):
    try:
        estabelecimentos = [Estabelecimentos(**
                            {
                                "cnpj_basico": data[0],
                                "cnpj_ordem": data[1],
                                "cnpj_dv": data[2],
                                "identificador": data[3],
                                "nome_fantasia": data[4],
                                "situacao_cadastral": data[5],
                                "data_situacao_cadastral": data[6],
                                "codigo_situacao_cadastral": data[7],
                                "nome_da_cidade_no_exterior": data[8],
                                "pais": data[9],
                                "data_de_inicio_atividade": data[10],
                                "cnae_fiscal_principal": data[11],
                                "cnae_fiscal_secundaria": data[12],
                                "tipo_de_logradouro": data[13],
                                "logradouro": data[14],
                                "numero": data[15],
                                "complemento": data[16],
                                "bairro": data[17],
                                "cep": data[18],
                                "uf": data[19],
                                "municipio": data[20],
                                "telefone_1": data[21]+data[22],
                                "telefone_2_": data[23]+data[24],
                                "e_mail": data[27],
                                "situacao_especial": data[28],
                                "data_da_situacao_especial": data[29]

                            }) for data in reader]
        logger.info(
            f'Inserindo estabelecimentos no banco de dados', also_console=True)
        logger.info(len(estabelecimentos), also_console=True)

        Estabelecimentos.objects.insert(estabelecimentos, load_bulk=False)

    except Exception as e:
        logger.info(f'Erro: {e}', also_console=True)


def inserir_socios(reader):
    try:
        socios = [Socios(**
                         {
                             "cnpj_basico":  data[0],
                             "identificador_de_socio": data[1],
                             "nome_do_socio": data[2],
                             "cnpj_ou_cpf": data[3],
                             "qualificacao_do_socio": data[4],
                             "data_de_entrada_sociedade": data[5],
                             "pais": data[6],
                             "representante_legal": data[7],
                             "nome_do_representante": data[8],
                             "qualificacao_representante_legal": data[9],
                             "faixa_etaria":  data[10]
                         }) for data in reader]
        logger.info(
            f'Inserindo socios no banco de dados', also_console=True)
        logger.info(len(socios), also_console=True)

        Socios.objects.insert(socios, load_bulk=True)

    except Exception as e:
        logger.info(f'Erro: {e}', also_console=True)
