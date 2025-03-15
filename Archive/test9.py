from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]


class Person(BaseModel):
    name: str
    surname: str

    @root_validator
    def check_name(cls, values):
        name = values['name']
        surname = values['surname']
        if name + ' ' + surname in FORBIDDEN_NAMES:
            raise ValueError('Такое имя не допустимо')


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    result = ' '.join([person.name, person.surname])
    result = result.title()
    return {'Hello': result}
