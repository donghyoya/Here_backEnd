from fastapi import FastAPI
from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"

database = Database(DATABASE_URL)
metadata = MetaData()

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()