from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from public.users import users_router
app = FastAPI()

app.include_router(users_router)

@app.get("/")
def f_indexH():
    return {"message": "Добро пожаловать! Это мой простой Web AP."}

