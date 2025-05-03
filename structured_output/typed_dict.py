from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person : Person = {'name': 'kartikay', 'age':21}
## new_person : Person = {'name': 'kartikay', 'age':21} this will also run no validation during runtime
print(new_person)    