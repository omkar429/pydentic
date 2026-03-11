from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import Optional, Dict
import pandas as pd


class test(BaseModel):
    name: str
    age: Optional[int] =  Field(default=20,gt=18, lt=100, strict=True)
    height: int
    email: EmailStr
    contact_detail : Dict[str, int]

    @field_validator('email')
    @classmethod
    def email(cls, value):
        vailde_domain = ['omkar.com','sun.com']

        domain_name = value.split('@')[-1]
        if domain_name not in vailde_domain:
            raise ValueError('Domain Not Fount Plz Enter vailde Domain')
        return value
    

    @field_validator('name')
    @classmethod
    def name(cls, value):
        data = value.upper()
        return data
    
    @model_validator(mode='after')
    def validetate(model):
        if model.age > 60:
            if 'emergency' not in model.contact_detail:
                raise ValueError('Eroo')
        return model
    

    @computed_field
    @property
    def nto(self) -> int:
        nto = self.age + self.height
        return nto



def pr(data: test):
    print(data.age)
    print(data.name)
    print(data.email)
    print(data.contact_detail)
    print(data.nto)


data = {
    'name': 'omkar',
    'age': 50,
    'email': 'omkar@omkar.com',
    'contact_detail': {'first_numer': 5432345,'emergency': 5434},
    'height': 6
}


all = test(**data)

pr(all)

print(all.email)

print(pd.DataFrame(all.model_dump()))