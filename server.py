from pymongo.mongo_client import MongoClient
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()

#-----------------------------/\ Deployment /\-------------------------------------#
#cf login
#cf push
#Local test : uvicorn server:app --reload

#------------------------------/\ Schemes /\---------------------------------------#
class book(BaseModel):
    _id:Optional[str]
    Title:str
    Autor:str
    Genero:str
    Synopsys:str
    Year: int
    Pages: int
    ISBN: int
    Editorial:str

    
def bookEntity(book) -> dict:
    return {
            "Title":book["Title"],
            "Autor":book["Autor"],
            "Genero":book["Genero"],
            "Synopsys":book["Synopsys"],
            "Year":book["Year"],
            "Pages": book["Pages"],
            "ISBN": book["ISBN"],
            "Editorial":book["Editorial"]
    }
    
def booksEntity(entity) -> list:
    return [bookEntity(book) for book in entity]
app = FastAPI()

@app.get("/")
async def hello():
    return "Hello World!"

@app.get("/books")
async def find_all_books():
    uri = os.getenv('URI')  
    # Create a new client and connect to the server
    client = MongoClient(uri)
    #Usar funcion getMongoDB
    DB_HOST = client["PythonTest"]
    # Seleccionar la colección
    collection = DB_HOST ["py"]
    # Insertar el document en la colección
    #inserted_id = collection.insert_one(doc)
    # Imprimir el ID del document insertado
    #print(inserted_id.inserted_id)
    Data = collection.find()
    return [bookEntity(book) for book in Data]
    #return "Hola Mundo"

