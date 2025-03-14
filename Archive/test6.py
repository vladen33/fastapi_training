from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class Tag(str, Enum):
    IMMUTABLE = 'immutable'
    MUTABLE = 'mutable'


@app.post('/a', tags=[Tag.IMMUTABLE],
          response_description='Функция возвращает строку',
          summary='1-я функция'
          )
def a() -> str:
    """
    :return: Функция возвращает str
    """
    return 'Вот это ответ!'


@app.get('/b', tags=[Tag.MUTABLE],
         response_description='Функция возвращает список',
         description='Функция возвращает список!!!',
         summary='2-я функция'
          )
def b() -> list:
    return ['Вот', 'это', 'ответ!']


@app.post('/c', tags=[Tag.IMMUTABLE],
          response_description='Функция возвращает число',
          summary='3-я функция'
          )
def c() -> int:
    """
    :return: Функция возвращает int
    """
    return 42


@app.get('/d', tags=[Tag.MUTABLE],
         response_description='Функция возвращает словарь',
         description='Функция возвращает словарь!!!',
         summary='4-я функция'
          )
def d() -> dict:
    return {'Вот': 'это ответ!'}