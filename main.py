from enum import Enum
from typing import Optional

from fastapi import FastAPI, Path, Query

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


@app.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия'
)
def greetings(
        *,
        # У параметров запроса name и surname значений по умолчанию нет,
        # поэтому в первый параметр ставим многоточие, Ellipsis.
        name: str = Path(
            ..., min_length=2, max_length=20,
            title='Полное имя', description='Можно вводить в любом регистре'
        ),
        surname: list[str] = Query(..., min_length=2, max_length=50),
        age: Optional[int] = Query(None, ge=5, le=99),
        is_staff: bool = Query(False, alias='is-staff', include_in_schema=False),
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

    surnames = '-'.join(surname)
    result = ' '.join([name, surnames])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
