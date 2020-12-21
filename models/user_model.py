from pydantic import BaseModel


class UserIn(BaseModel): #post
    user: str
    password: str


class userIn(BaseModel): #GET
    user: str
    password: str
    name: str
    email: str

class userOut(BaseModel): #POST/
    name: str
    user: str
    email: str

class UserInCrear(BaseModel): #GET
    user: str
    password: str
    name: str
    email: str
