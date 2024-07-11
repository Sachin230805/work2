from fastapi import FastAPI,Body,status,HTTPException,Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import time
 

app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
class User(BaseModel):
    name: str
    age: int
    company_name: str = None
    id:int



users=[{"name":"SACHIN","age":18,"company_name":"SEEDFLEX","id":10},{"name":"WADZEE","age":23,"company_name":"SEEDFLEX","id":12},
      {"name":"ADITYA","age":36,"company_name":"SEEDFLEX","id":13},{"name":"ADAM","age":28,"company_name":"SEEDFLEX","id":14},
      {"name":"GEORGE","age":37,"company_name":"SEEDFLEX","id":15},{"name":"MUSTAFA","age":53,"company_name":"SEEDFLEX","id":16}]
     

@app.get("/")
def main_page():
    return("WELCOME TO SEEDFLEX")