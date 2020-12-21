from typing import Dict
from pydantic import BaseModel

class User(BaseModel):
    name: str
    user: str
    password: str
    email: str

database_users = Dict[str, User]
database_users = {"pao123":User(**{
                                "user": "pao123",
                                "password": "1234",
                                "name":"Paola",
                                "email": "p@correo.com" }),
                "fran123":User(**{
                                "user": "fran123",
                                "password": "250ss3fd",
                                "name":"Francisco",
                                "email": "f@correo.com" }),
                "esteb3":User(**{
                                "user": "esteb3",
                                "password": "abcdef",
                                "name":"Esteban",
                                "email": "e@correo.com" }),
                "ivan123":User(**{
                                "user": "ivan123",
                                "password": "1234",
                                "name":"Ivan",
                                "email": "i@correo.com" }),
                }

def get_user(user: str):
    if user in database_users.keys():
        return database_users[user]
    else:
        return None

def update_user(user_in_db: User):
    database_users[user_in_db.user] = user_in_db
    return user_in_db

def register_user(user_in_db: User):
    if user_in_db.user in database_users.keys():
        return "Usuario existente"
    else:
        a = {user_in_db.user: user_in_db}
        database_users.update(a)
        return a

