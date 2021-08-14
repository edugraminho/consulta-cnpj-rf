import os
import hvac
from hvac.exceptions import InvalidPath
from requests.exceptions import ConnectionError
from robot.api import logger


def get_credentials(secrets_path):
    client = __client()
    return __get_secrets(client, secrets_path)


def __client():
    token = os.environ.get('HCV_TOKEN')
    try:
        client = hvac.Client(
            token=token
        )
        if not client.is_authenticated():
            raise ValueError('Verifique o token configurado na variável de'
                             ' ambiente')
        return client
    except ConnectionError as e:
        msg = 'Verifique se o Vault está em execução e se as variáveis de '
        'ambiente, descritas na documentação dessa Lib, estão configuradas.'
        logger.error(f'{e}\n{msg}')
        raise ValueError(msg)


def __get_secrets(client, path):
    try:
        hvreponse = \
            client.secrets.kv.read_secret_version(path=path)
        return hvreponse['data']['data']
    except InvalidPath as e:
        msg = f'Verifique se o path {path} está criado no vault seguindo o '
        f'padrão da documentação dessa lib'
        logger.error(f'{e}\n{msg}')
    except KeyError as e:
        logger.error(f'Ocorreu um erro ao extrair os dados da '
                     f'reposta {hvreponse}\n '
                     f'Verifique a resposta.')
        raise e
