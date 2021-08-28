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
