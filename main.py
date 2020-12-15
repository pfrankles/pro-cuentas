from fastapi import FastAPI 
from pydantic import BaseModel
from models.user_model import userIn,UserIn,userOut
from db.user_db import User, get_user
from db.user_db import update_user, register_user
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# origins = ["http://localhost","http://localhost:8080","http://127.0.0.1:8000",
#             "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
#             "http://127.0.0.1:8000/user/auth/"]

app.add_middleware(
     CORSMiddleware, 
     allow_origins=["*"],
     allow_credentials=True, 
     allow_methods=["*"], 
     allow_headers=["*"],   
)

@app.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.user)
    if user_in_db == None:
        return {"Autenticado": False}
    
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    
    return {"Autenticado": True}


@app.get("/user/get_name/{user}")
async def get_name(user: str):
    user_in_db = get_user(user)
    
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario " +user+  " no existe")
    
    user_out = userOut(**user_in_db.dict())
    return user_out


@app.put("/user/update/")
async def update_user(user_select: userIn):
    user_in = get_user(user_select.user)
    
    if user_in == None: 
        raise HTTPException(status_code=404, detail="Usuario ya existe")
    
    user_in.name = user_select.name
    user_in.user = user_select.user
    user_in.password = user_select.password
    user_in.email = user_select.email
    update_user(user_in)
    user_out = userOut(**user_in.dict())
    return user_out


@app.put("/user/register/")
async def register_user(user_select: userIn):
    
    user_in = get_user(user_select.user)

    if user_in != None: 
        raise HTTPException(status_code=404, detail="Usuario ya existe")
    
    else:
        transaction_user = register_user(User(**user_select.dict()))

        user_out = userOut(**user_select.dict())
        return user_out
        
       