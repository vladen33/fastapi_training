from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

class EducationLevel(str, Enum):
    # Укажем значения с большой буквы, чтобы они хорошо смотрелись
    # в документации Swagger.
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me', tags=['special methods'], summary='Приветствие автора')
def hello_author():
    return {'Hello': 'author'}


@app.get('/{name}', tags=['common methods'], summary='Общее приветствие')
def greetings(
        *,
        name: str,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False,
        education_level: Optional[EducationLevel] = None,
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
