# pip install pydantic
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: int = 18 # default valu
    gender: Optional[str] = None # optional field 
    # Implicit type conversion : Type Coersion
    number: int = 0
    # Build in validation like email, url, etc can be used from pydantic
    email: EmailStr 
    gpa: float = Field(ge=0.0, le=4.0, description="Representing CGPA", default=0) # gpa should be between 0.0 and 4.0

# number will be converted to int pydantic TypeCoersion
new_student = Student(name="John Doe",gender="Male",number="123",email="abs@gmail.com",gpa=3.5)
print(new_student)

# Convert to dict or json
print(dict(new_student))
print(new_student.model_dump_json)