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

# Delete doctor details
def delete_doctor():
    doctor_id = int(input("Enter Doctor's ID to delete: "))
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()

    if doctor:
        session.delete(doctor)
        session.commit()
        print(f"Doctor with ID {doctor_id} deleted successfully.")
    else:
        print("Doctor with that ID not found.")

# List all doctors
def list_doctors():
    doctors = session.query(Doctor).all()
    if doctors:
        for doctor in doctors:
            print(f"ID: {doctor.id}, Name: {doctor.name}, Age: {doctor.age}, Department: {doctor.department}")
            print(" ")
    else:
        print("No doctors found.")

# Create a new patient
def create_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    phone_number = input("Enter patient phone number: ")
    email = input("Enter patient email: ")
    adm_number = input("Enter patient admission number: ")
    ward_name = input("Enter patient ward name: ")
    doctor_id = int(input("Enter doctor ID for this patient: "))

    # Check if the doctor exists
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()
    
    if doctor:
        patient = Patient(
            name=name,
            age=age,
            phone_number=phone_number,
            email=email,
            adm_number=adm_number,
            ward_name=ward_name,
            doctor_id=doctor.id  # Link to the doctor
        )
        session.add(patient)
        session.commit()
        print(f"Patient '{name}' created successfully with ID: {patient.id}")
        return patient
    else:
        print(f"Doctor with ID {doctor_id} not found. Patient creation failed.")

# Read patient details

# List all patients
def list_patients():
    patients = session.query(Patient).all()
    if patients:
        for patient in patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Ward: {patient.ward_name}, Doctor: {patient.doctor.name}")
            print(" ")
    else:
        print("No patients found.")

# Run the database initialization if needed
if __name__ == "__main__":
    init_database()  # Uncomment this if you want to initialize the database on first run

    # Example usage of the functions:
    # Create a doctor, then a patient for that doctor
    create_doctor()
    update_doctor()
    create_patient()
    update_patient()
    list_doctors()
    list_patients()
