import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("connection_string")

engine = create_engine(connection_string)
# creating a session
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

