from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, Literal, Annotated


class test(BaseModel):
    name: Annotated[str, Field(description='Name of the canditant')] 
    gender: Annotated[str,Literal['male','female'], Field(description='Gender of the candidet')]
    age: Annotated[int, Field(gt=0, lt=120, description='Enter the age of the candidet')]
    email: Annotated[EmailStr, Field(description='Age of the candidate')]
    contact:Annotated[Dict[str, str], Field(description='Enter the conatact detail for the candidet')]
    height: Annotated[float, Field(gt=0, description='hegiht of the caditete in meter')]
    weight: Annotated[float, Field(gt=0, description='weight of the candidat in KG')]

    @field_validator('name')
    @classmethod
    def name(cls, value):
        valus = value.upper()
        return valus
    
    @field_validator('email')
    @classmethod
    def email(cls, value):
        vailed_data = ['omkar.com','hdfc.com']
        email_data = value.split('@')[-1]

        if email_data not in vailed_data:
            raise ValueError('Not a Vailed Domain')
        return value
    
    @model_validator(mode='after')
    def contact(model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('plz provide the costuem emergency number costomer age is greate then 60 ')
        
        return model
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height**2)
        return bmi


data = {
    'name': 'omkar',
    'gender': 'male',
    'age': 80,
    'email': 'omkar@hdfc.com',
    'contact': {
        'first_contact': '765432676',
        'emergency': '65434567'
    },
    'height': 43,
    'weight': 54 

}


all = test(**data)
 
print(all.name)
print(all.gender)
print(all.age)
print(all.email)
print(all.contact)
print(all.height)
print(all.weight)
print(all.bmi)