from app import app
from .database import create_db_and_tables
from .database import (
    Hero,
    ENGINE,
)
from sqlmodel import (
    Session,
    select
)
from typing import (
    List
)

@app.on_event('startup')
async def startup():
    create_db_and_tables()


@app.get(
    '/'
)
async def main():
    return {'message': 'Hello World'}


@app.post(
    "/heroes/",
    response_model = Hero
)
def create_hero(hero: Hero):
    '''
        Endpoint to create a hero
    '''
    with Session(ENGINE) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero
    
@app.get(
    "/heroes/",
    response_model=List[Hero]
)
def read_heroes():
    '''
        Endpoint to get all heroes
    '''
    with Session(ENGINE) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes