from datetime import datetime, date
from mongoengine import EmbeddedDocument, DateTimeField, IntField, \
    BooleanField, StringField, EnumField, Document, FloatField, ListField, \
    EmbeddedDocumentField, ObjectIdField, DynamicDocument, DynamicField, \
    ReferenceField
from Variables.config import *
 

class Empresas(Document):
    cnpj_basico = IntField(required=True, unique=False)
    razao_social = StringField(required=False)
    natureza_juridica = IntField(required=False)
    qualificacao_do_responsavel = IntField(required=False)
    capital_social_da_empresa = IntField(required=False)
    porte_da_empresa = IntField(required=False)

    meta = {'collection': 'empresas', 'db_alias': AREA_NAME}


class Estabelecimentos(Document):
    cnpj_basico = IntField(required=True, unique=False)
    cnpj_ordem = IntField(required=False)
    cnpj_dv = IntField(required=False)
    identificador = IntField(required=False)
    nome_fantasia = StringField(required=False)
    situacao_cadastral = IntField(required=False)
    data_situacao_cadastral = StringField(required=False)
    codigo_situacao_cadastral = IntField(required=False)
    nome_da_cidade_no_exterior = StringField(required=False)
    pais = StringField(required=False)
    data_de_inicio_atividade = StringField(required=False)
    cnae_fiscal_principal = StringField(required=False)
    cnae_fiscal_secundaria = StringField(required=False)
    tipo_de_logradouro = StringField(required=False)
    logradouro = StringField(required=False)
    numero = StringField(required=False)
    complemento = StringField(required=False)
    bairro = StringField(required=False)
    cep = IntField(required=False)
    uf = StringField(required=False)
    municipio = StringField(required=False)
    telefone_1 = IntField(required=False)
    telefone_2_ = IntField(required=False)
    e_mail = StringField(required=False)
    situacao_especial = StringField(required=False)
    data_da_situacao_especial = StringField(required=False)


    meta = {'collection': 'estabelecimentos', 'db_alias': AREA_NAME}


class Socios(Document):
    cnpj_basico = IntField(required=True, unique=False) 
    identificador_de_socio = IntField(required=False)
    nome_do_socio = StringField(required=False)
    cnpj_ou_cpf = StringField(required=False)
    qualificacao_do_socio = IntField(required=False)
    data_de_entrada_sociedade = StringField(required=False)
    pais = StringField(required=False)
    representante_legal = StringField(required=False)
    nome_do_representante = StringField(required=False)
    qualificacao_representante_legal = IntField(required=False)
    faixa_etaria = IntField(required=False)

    meta = {'collection': 'socios', 'db_alias': AREA_NAME}
