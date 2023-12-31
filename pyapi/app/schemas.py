from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreated(PostBase):
    pass 

class Post(PostBase):
    # title : str
    # content : str
    # published : bool
    class Config:
        orm_mode=True

class UserCreated(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    email : EmailStr
    id : int
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None
