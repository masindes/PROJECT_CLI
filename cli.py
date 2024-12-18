import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Doctor, Patient  # Assuming you have a 'models' module

# Database URL
DATABASE_URL = 'sqlite:///doctors.db'

# Set up engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize the database
def init_database():
    Base.metadata.create_all(engine)
    print("Database created and tables initialized.")

# Create a new doctor
def create_doctor():
    name = input("Enter Doctor's name: ")
    age = int(input("Enter Doctor's age: "))
    phone_number = input("Enter Doctor's phone number: ")
    email = input("Enter Doctor's email: ")
    hospital_id = int(input("Enter Doctor's hospital id: "))
    department = input("Enter Doctor's department: ")

    doctor = Doctor(
        name=name,
        age=age,
        phone_number=phone_number,
        email=email,
        hospital_id=hospital_id,
        department=department
    )
    
    session.add(doctor)
    session.commit()
    print(f"Doctor '{name}' created successfully with ID: {doctor.id}")

# Update doctor details
def update_doctor():
    doctor_id = int(input("Enter Doctor's ID to update: "))
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()

    if doctor:
        print(f"Updating details for Doctor: {doctor.name}")
        doctor.name = input(f"Enter new name (current: {doctor.name}): ") or doctor.name
        doctor.age = int(input(f"Enter new age (current: {doctor.age}): ") or doctor.age)
        doctor.phone_number = input(f"Enter new phone number (current: {doctor.phone_number}): ") or doctor.phone_number
        doctor.email = input(f"Enter new email (current: {doctor.email}): ") or doctor.email
        doctor.hospital_id = int(input(f"Enter new hospital id (current: {doctor.hospital_id}): ") or doctor.hospital_id)
        doctor.department = input(f"Enter new department (current: {doctor.department}): ") or doctor.department
        
        session.commit()
        print(f"Doctor {doctor.name} updated successfully!")
    else:
        print("Doctor with that ID not found.")

# Run the database initialization if needed
if __name__ == "__main__":
    init_database()  # Uncomment this if you want to initialize the database on first run

    # Example usage of the functions:
    create_doctor()
    update_doctor()
