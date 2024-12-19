import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Doctor, Patient  
from terminaltables import AsciiTable  

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

# Delete Doctor details
def delete_doctor():
    doctor_id = int(input("Enter Doctor's ID to delete: "))
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()

    if doctor:
        # Delete all associated patients before deleting the doctor
        patients = session.query(Patient).filter(Patient.doctor_id == doctor_id).all()
        for patient in patients:
            session.delete(patient)
        
        session.delete(doctor)
        session.commit()
        print(f"Doctor with ID {doctor_id} and their associated patients have been deleted successfully.")
    else:
        print("Doctor with that ID not found.")

# List all doctors (using terminaltables to format the table)
def list_doctors():
    doctors = session.query(Doctor).all()
    if doctors:
        table_data = [['ID', 'Name', 'Age', 'Department']]  # Table headers
        for doctor in doctors:
            table_data.append([doctor.id, doctor.name, doctor.age, doctor.department])

        table = AsciiTable(table_data)  # Create the table
        print(table.table)  # Print the table
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
    doctor_id = int(input("Enter doctor_id: "))
    
    # Find the doctor by the doctor_id
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
        print(f"Patient '{name}' created successfully under Doctor '{doctor.name}' with ID: {patient.id}")
    else:
        print(f"Doctor with ID {doctor_id} not found. Patient creation failed.")

# Read a patient's details
def read_patient():
    patient_id = int(input("Enter patient ID to read: "))
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        print(f"Patient ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Doctor: {patient.doctor.name}")
    else:
        print("Patient with that ID not found.")

# Update patient details
def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    patient = session.query(Patient).filter(Patient.id == patient_id).first()

    if patient:
        print(f"Updating details for Patient: {patient.name}")
        patient.name = input(f"Enter new name (current: {patient.name}): ") or patient.name
        patient.age = int(input(f"Enter new age (current: {patient.age}): ") or patient.age)
        patient.phone_number = input(f"Enter new phone number (current: {patient.phone_number}): ") or patient.phone_number
        patient.email = input(f"Enter new email (current: {patient.email}): ") or patient.email
        patient.adm_number = input(f"Enter new admission number (current: {patient.adm_number}): ") or patient.adm_number
        patient.ward_name = input(f"Enter new ward name (current: {patient.ward_name}): ") or patient.ward_name
        patient.doctor_id = int(input(f"Enter new doctor_id (current: {patient.doctor_id}): ") or patient.doctor_id)

        session.commit()
        print(f"Patient {patient.name} updated successfully!")
    else:
        print("Patient with that ID not found.")

# Delete a patient's details
def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))
    patient = session.query(Patient).filter(Patient.id == patient_id).first()

    if patient:
        session.delete(patient)
        session.commit()
        print(f"Patient with ID {patient_id} deleted successfully.")
    else:
        print("Patient with that ID not found.")

# List all patients under a doctor (using terminaltables to format the table)
def list_patients():
    doctor_id = int(input("Enter Doctor's ID to list patients: "))
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()

    if doctor:
        patients = doctor.patients  # Accessing the patients via the relationship
        if patients:
            table_data = [['Patient ID', 'Name', 'Age', 'Ward']]  
            for patient in patients:
                table_data.append([patient.id, patient.name, patient.age, patient.ward_name])

            table = AsciiTable(table_data)  
            print(table.table) 
        else:
            print(f"No patients found for Doctor {doctor.name}.")
    else:
        print("Doctor with that ID not found.")

# Main Menu Function
def main_menu():
    while True:
        print("\nWelcome to Patient Management System, How may I help?")
        print("1. Add a new Doctor")
        print("2. Update Doctor details")
        print("3. Delete Doctor details")
        print("4. List all doctors")
        print("5. Add a new Patient")
        print("6. Read a Patient's details")
        print("7. Update Patient details")
        print("8. Delete Patient details")
        print("9. List all patients under a doctor")
        print("10. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_doctor()  
        elif choice == "2":
            update_doctor()
        elif choice == "3":
            delete_doctor()
        elif choice == "4":
            list_doctors()
        elif choice == "5":
            create_patient()
        elif choice == "6":
            read_patient()
        elif choice == "7":
            update_patient()
        elif choice == "8":
            delete_patient()
        elif choice == "9":
            list_patients()
        elif choice == "10":
            print("Thank you for using the Patient Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Database initialization 
if __name__ == "__main__":
    init_database() 
    
    # Start the main menu
    main_menu()
