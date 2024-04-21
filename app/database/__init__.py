from sqlmodel import (
    create_engine, 
    SQLModel, 
    Session, 
    Field, 
    select,
)
from typing import (
    Optional,
)



ENGINE = create_engine(
    "postgresql+psycopg2://citizix_user:S3cret@localhost/citizix_db"
)


