from dotenv import dotenv_values
import logging

__config__ = dotenv_values(".env")

USERNAME_DATABASE = __config__.get('USERNAME_DATABASE')
PASSWORD_DATABASE = __config__.get('PASSWORD_DATABASE')
NAME_DATABASE     = __config__.get('NAME_DATABASE')


logging.basicConfig(
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
)

