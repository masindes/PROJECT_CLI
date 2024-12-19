
# **Patient Management System**
This is a Patient Management System that allows users to manage doctor and patient records. The system supports functionalities like adding, updating, deleting, and listing doctors and patients. It uses SQLAlchemy to interact with an SQLite database and terminaltables to format the output in a table-like structure for better readability.

# **Features**

The User can:

. Add, update, delete, and list doctors.

. Add, update, delete, and list patients.

. Link patients to specific doctors.

. View a patient's details and the doctors associated with them.

# **Requirements**

-Python 3.x

-SQLAlchemy

-Terminaltables

-Sqlite3

# **Functionality**

**Doctor Operations**

Add a Doctor: Creates a new doctor by entering their name, age, phone number, email, hospital ID, and department.

Update a Doctor: Updates an existing doctor's details by specifying their ID.

Delete a Doctor: Deletes a doctor and all associated patients by specifying their ID.

List all Doctors: Displays a list of all doctors in a table format.

**Patient Operations**

Add a Patient: Creates a new patient and links them to a specific doctor. Requires the patient's details and the doctor's ID.

Read a Patient's Details: Displays the details of a patient based on their ID.

Update a Patient: Updates an existing patient's details by specifying their ID.

Delete a Patient: Deletes a patient based on their ID.

List all Patients under a Doctor: Lists all patients associated with a specific doctor.


# **Setup**
To run the application, follow these steps:
1. Clone the repository
2. Install the dependencies by running pipenv install, sqlalchemy alembic 
3. Start the application by running python cli.py
4. Use the provided commands to interact with the system

# **API Documentation**
The application uses a mock API for demonstration purposes. The API endpoints are as follows:
-GET /jobs: Returns a list of all jobs
-GET /jobs/:id: Returns a single job by id
-POST /jobs: Creates a new job
-PATCH /jobs/:id: Updates a job
-DELETE /jobs/:id: Deletes a job

# **Installation**
To install the dependencies, run the following command:
1 . npm install
# **Usage**
To start the application, run the following command:
1 . npm start


# **Contribution**
If you have suggestion or find an issue.Feel free to submit a pull request.
I value your feedback here and I will appreciate your contribution!
1.Fork the project
2.Create a new branch
3.commit your changes.
4.push to the branch
# **Contact**
[Masinde  Sylvester][masinde.sylvester@yahoo.com]

# **License**
This project is licensed under MIT


# **Repo link**

https://github.com/masindes/PROJECT_CLI

