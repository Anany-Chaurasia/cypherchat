from pydantic import BaseModel

class User_Register(BaseModel):
    email: str
    password: str

class User_Login(BaseModel):
    email: str
    password: str

class User_Update(BaseModel):
    email: str | None = None
    password: str | None = None
    age: int | None = None
    bio: str | None = None
    
