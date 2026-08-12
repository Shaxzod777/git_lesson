from datetime import datetime
from pydantic import BaseModel,EmailStr,Field


class UserCreate(BaseModel):
    full_name:str=Field(...,min_length=3,max_length=100)
    email:EmailStr
    password:str=Field(...,min_length=8)
    phone:str=Field(max_length=17)
    address:str|None=None


class UserOute(BaseModel):
    id:int
    full_name:str
    email:EmailStr
    phone:str
    address:str|None=None

    class Config:
        from_attributes=True


class Token(BaseModel):
    access_token:str
    token_type:str="bearer"


