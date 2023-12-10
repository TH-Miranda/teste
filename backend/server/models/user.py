from pydantic import BaseModel

class UserProfile(BaseModel):
    email: str
    age: int
    first_name: str
    second_name: str
    height: float
    weight: float
    age: int
    gender: str
