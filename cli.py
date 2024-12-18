import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Doctor, Patient


DATABASE_URL = 'sqlite://doctors.db'

engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)