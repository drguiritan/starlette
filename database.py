from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

cons_str ="sqlite:///" +  os.path.join(BASE_DIR,"students.db")

Base = declarative_base()

Engine = create_engine(
    cons_str,
    echo=True,
)
