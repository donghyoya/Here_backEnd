from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)