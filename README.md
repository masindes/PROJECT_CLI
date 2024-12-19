**Patient Management System **
Overview

The Patient Management System is a Python-based application that allows users to manage doctors and patients in a healthcare setting. This system interacts with an SQLite database to store doctor and patient information, and provides functionality to add, update, delete, and view details of doctors and patients. It uses SQLAlchemy for ORM (Object Relational Mapping) and terminaltables for displaying data in a tabular format in the terminal.

Features
1.Doctor Management: Add new doctors Update doctor details Delete doctor details along with their associated patients List all doctors 1.Patient Management: Add new patients under a specific doctor Read patient details Update patient details Delete patient details List all patients under a specific doctor

Features
Users can view all jobs
Users can view a single job
Users can add a new job
Users can edit a job
Users can delete a job
Requirements
Python
SQLite
SQLAlchemy
terminaltables
Functionality
Doctor Management: Add a new Doctor: The user can enter the doctor’s details (name, age, phone number, email, hospital ID, and department) to create a new doctor. Update Doctor Details: The user can update a doctor’s information by specifying the doctor’s ID. Delete Doctor: The user can delete a doctor’s record by ID. All associated patients will also be deleted. List Doctors: Display a list of all doctors in a formatted table showing their ID, name, age, and department.
Patient Management: Add a new Patient: The user can create a new patient by providing the patient’s details (name, age, phone number, email, admission number, ward name, and doctor ID). Read Patient Details: The user can view details of a specific patient by ID. Update Patient Details: The user can update the details of an existing patient. Delete Patient: The user can delete a patient’s record by ID. List Patients of a Doctor: The user can list all patients under a specific doctor using the doctor’s ID.
Setup and Installation
Clone or Download the repository: Clone this repository to your local machine or download the patient_management_system.py file.
Database: The application uses SQLite as the database (doctors.db). Upon running the application, the database file and tables will be created automatically.
Run the Application: To start the application, run the Python script: python cli.py
Installation
To install the dependencies, run the following command: 1 . pipenv install sqlalchemy alembic

Usage
To start the application, run the following command: 1 .

Contribution
If you have suggestion or find an issue.Feel free to submit a pull request. I value your feedback here and I will appreciate your contribution! 1.Fork the project 2.Create a new branch 3.commit your changes. 4.push to the branch

Contact
[Masinde Sylvester][masinde.sylvester@yahoo.com]

License
This project is licensed under MIT
