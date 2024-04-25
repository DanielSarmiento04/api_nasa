from sqlmodel import (
    create_engine, 
    SQLModel, 

)
from typing import (
    Optional,
)
from ..constants import (
    NAME_DATABASE,
    PASSWORD_DATABASE,
    USERNAME_DATABASE,
)
from .hero import (
    Hero
)

# connect_args = {"check_same_thread": False}

ENGINE = create_engine(
    f"postgresql+psycopg2://{USERNAME_DATABASE}:{PASSWORD_DATABASE}@localhost/{NAME_DATABASE}",
    echo=True, 
    # connect_args=connect_args,
)


def create_db_and_tables():
    '''
    '''
    SQLModel.metadata.create_all(ENGINE)
