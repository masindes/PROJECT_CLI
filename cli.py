import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Doctor, Patient


DATABASE_URL = 'sqlite://doctors.db'

engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)
session = sessionmaker()

# initialize database
def init_database():
    Base.metadata.create_all(engine)
    print("Database created and tables initialized.")

# create database
def create_doctor():
    name = input("Enter Doctor's name")
    age = int(input("Enter Doctor's age"))
    phone_number = input("Enter Doctor's phone number")
    email = input("Enter Doctor's email")
    hospital_id = int(input("Enter Doctor's hospital id"))
    department = int(input("Enter Doctor's department"))
    doctor = Doctor(name=name, age=age, phone_number=phone_number, email=email, hospital_id=hospital_id, department=department)
    session.add(doctor)
    session.commit()
    print(f"Doctor '{name}' created successfully with '{doctor.id}'")