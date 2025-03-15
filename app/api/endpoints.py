# api/endpoints.py
# Импортируем класс API роутера.
from fastapi import APIRouter, Body

from app.schemas.schemas import Person

# Создаём объект роутера.
router = APIRouter()


# В декораторе подставляем объект роутера вместо app.
@router.post('/hello')
def greetings(
        person: Person = Body(
            ...,
            examples=Person.Config.schema_extra['examples']
        )
) -> dict[str, str]:
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
