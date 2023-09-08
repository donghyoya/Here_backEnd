from sqlalchemy.orm import sessionmaker, Session
from default.config import database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database.engine)
