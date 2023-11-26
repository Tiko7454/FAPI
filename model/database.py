import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = os.getenv('FAPI_DB_URL')
# assert SQLALCHEMY_DATABASE_URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:pass123@localhost"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()