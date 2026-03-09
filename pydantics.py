from pydantic import BaseModel

class T(BaseModel):
    name: str
    age: int
    last_name: str


def print1(data: T):
    print(data.age)
    print(data.name)
    print(data.last_name)


name = 'omkar'
last_name = 'kushwaha'
age = '20'


data = T(name=name, age=age, last_name=last_name)

print1(data=data)