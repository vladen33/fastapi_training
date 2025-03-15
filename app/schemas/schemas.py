import re
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, root_validator, validator


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str = Field(..., max_length=20)
    surname: Union[str, list[str]] = Field(..., max_length=50)
    age: Optional[int] = Field(None, gt=4, le=99)
    is_staff: bool = Field(False, alias='is-staff')
    education_level: Optional[EducationLevel]

    class Config:
        title = 'Класс для приветствия'
        min_anystr_length = 2
        schema_extra = {
           'example': {
               'name': 'Eduardo',
               'surname': ['Santos', 'Tavares'],
               'age': 20,
               'is_staff': False,
               'education_level': 'Среднее образование'
           }
        }

    @validator('name')
    def name_cant_be_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError('Имя не может быть числом')
        return value

    @root_validator
    # К названию параметров функции-валидатора нет строгих требований.
    # Первым передается класс, вторым — словарь со значениями всех полей.
    def using_different_languages(cls, values):
        # Объединяем все фамилии в единую строку.
        # Даже если values['surname'] — это строка, ошибки не будет,
        # просто все буквы заново объединятся в строку.
        surname = ''.join(values['surname'])
        # Объединяем имя и фамилию в единую строку.
        checked_value = values['name'] + surname
        # Ищем хотя бы одну кириллическую букву в строке
        # и хотя бы одну латинскую букву.
        # Флаг re.IGNORECASE указывает на то, что регистр не важен.
        if (re.search('[а-я]', checked_value, re.IGNORECASE)
                and re.search('[a-z]', checked_value, re.IGNORECASE)):
            raise ValueError(
                'Пожалуйста, не смешивайте русские и латинские буквы'
            )
        # Если проверка пройдена, возвращается словарь со всеми значениями.
        return values


