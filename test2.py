from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional

class test(BaseModel):
    name: str
    age: Optional[int] = Field(strict=True)
    email: EmailStr

    @field_validator('email')
    @classmethod
    def email(cls, value):
        vailed_domain = ['hdfc.com','icic.com']
        domain_name = value.split('@')[-1]
        if domain_name not in vailed_domain:
            raise ValueError('Not a valid domain')
        return value



def test1(data: test):
    print(data.age)
    print(data.name)
    print(data.email)



name = 'omkar'
age = 43
email = 'omkarkushwaha@icic.com'

data = test(name=name, age=age, email=email)

test1(data=data)