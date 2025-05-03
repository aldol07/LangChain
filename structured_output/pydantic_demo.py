from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,default=5,description="represent cgpa of student")



new_student = {'name':'Kartikay','age':21,'email':'abcd@gmail.com','cgpa':2}   

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()