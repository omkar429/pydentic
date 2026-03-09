from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional

class test(BaseModel):
    name: Optional[str] = Field(default='nothing', max_length=10)
    age: int
    weight: float = Field(gt=0, strict=True)
    detail: List[str]
    contants: Dict
    email: EmailStr

def pr(data: test):
    print(data.age)
    print(data.name)
    print(data.weight)
    print(data.detail)
    print(data.contants)
    print(data.email)

name= 'omkar'
age = 20
wight = 19
detail = ['red','blue','greed','black']
contants = {
    'name': ['omkar','kushwaha'],
    'age': 23
}
email = 'omkark@uswaha7138gmail.com'

d = test(name=name ,age=age, weight=wight, contants=contants, detail=detail, email=email)
pr(data=d)
print('*'*100)
