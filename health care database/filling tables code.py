import random
from faker import Faker
import mysql.connector

host = 'localhost'
user = "root"
password = '0000'
database = 'health_care'
# Establish a connection to your MySQL database
# Replace the placeholders with your own database credentials
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create an instance of the Faker class
fake = Faker()
cursor = connection.cursor()

# Generate fake data for Login table
login_data = []
for i in range(1020):
    username = fake.user_name() + str(i)
    password = fake.password()
    login_data.append((i, username, password))

# Generate fake data for Patients table

patients_data = []
for i in range(1000):
    id = i
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = random.choice(["Male", "Female"])
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
    phone_number = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    city = fake.city()
    state = fake.state()
    country = fake.country()
    postal_code = fake.postcode()
    patients_data.append((id, first_name, last_name, gender, date_of_birth, phone_number,
                          address, city, state, country, postal_code))

# Generate fake data for Doctors table
doctors_data = []
for i in range(20):
    id = i
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = random.choice(["Male", "Female"])
    date_of_birth = fake.date_of_birth(minimum_age=30, maximum_age=70)
    phone_number = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    city = fake.city()
    state = fake.state()
    country = fake.country()
    postal_code = fake.postcode()
    specialization = fake.job()
    doctors_data.append((id, first_name, last_name, gender, date_of_birth, phone_number,
                         address, city, state, country, postal_code, specialization))

# Generate fake data for other tables (Medications, LabTests, InsuranceCompanies, etc.)
# ... (Code for generating fake data for other tables)


# Generate fake data for Medications table
medications_data = []
for id in range(100):
    medication_name = fake.word()
    medications_data.append((id, medication_name,))

# Generate fake data for LabTests table
lab_tests_data = []
for id in range(50):
    test_name = fake.word()
    lab_tests_data.append((id, test_name,))

# Generate fake data for InsuranceCompanies table
insurance_companies_data = []
for id in range(10):
    company_name = fake.company()
    address = fake.address().replace("\n", ", ")
    city = fake.city()
    state = fake.state()
    country = fake.country()
    postal_code = fake.postcode()
    insurance_companies_data.append((id, company_name, address, city, state, country, postal_code))

# Generate fake data for Prescriptions table
prescriptions_data = []
for i in range(1000):
    prescription_id = i
    # Fetch valid appointment IDs from the appointments table
    cursor.execute("SELECT AppointmentID FROM appointments")
    valid_appointment_ids = cursor.fetchall()
    # Choose a random valid appointment ID
    appointment_id = random.choice(valid_appointment_ids)[0]
    patient_id = random.randint(1, 500)
    # Fetch valid doctor IDs from the doctors table
    cursor.execute("SELECT DoctorID FROM doctors")
    valid_doctor_ids = cursor.fetchall()
    # Choose a random valid doctor ID
    doctor_id = random.choice(valid_doctor_ids)[0]
    prescription_date = fake.date_between(start_date="-1y", end_date="today")
    prescriptions_data.append((prescription_id, appointment_id, patient_id, doctor_id, prescription_date))
    
# Generate fake data for PrescriptionMedications table
prescription_medications_data = []
for i in range(1000):
    prescription_id = i
    # Fetch valid medication IDs from the medications table
    cursor.execute("SELECT MedicationID FROM medications")
    valid_medication_ids = cursor.fetchall()
    # Choose a random valid medication ID
    medication_id = random.choice(valid_medication_ids)[0]
    dosage = fake.random_int(min=1, max=4)
    frequency = fake.random_element(elements=("Once a day", "Twice a day", "Three times a day", "As needed"))
    prescription_medications_data.append((prescription_id, medication_id, dosage, frequency))

# Generate fake data for Payments table
payments_data = []
for i in range(1000):
    payment_id = i
    PatientID = random.randint(0, 999)
    amount = round(random.uniform(20, 200), 2)
    payment_date = fake.date_between(start_date="-1y", end_date="today")
    payments_data.append((payment_id, appointment_id, amount, payment_date))

# Generate fake data for MedicalRecords table
medical_records_data = []
for i in range(1000):
    record_id = i
    patient_id = random.randint(1, 500)
    # Fetch valid doctor IDs from the doctors table
    cursor.execute("SELECT DoctorID FROM doctors")
    valid_doctor_ids = cursor.fetchall()
    # Choose a random valid doctor ID
    doctor_id = random.choice(valid_doctor_ids)[0]
    appointment_id = random.randint(1, 500)
    diagnosis = fake.text(max_nb_chars=100)
    treatment = fake.text(max_nb_chars=100)
    medical_records_data.append((record_id, patient_id, doctor_id, appointment_id, diagnosis, treatment))

# Generate fake data for LabResults table
lab_results_data = []
for i in range(1000):
    result_id = i
    lab_test_id = random.randint(0, 49)
    patient_id = random.randint(0, 999)
    result = fake.text(max_nb_chars=100)
    lab_results_data.append((result_id, lab_test_id, patient_id, result))

# Generate fake data for InsurancePolicies table
insurance_policies_data = []
for i in range(999):
    policy_id = i
    patient_id = i
    company_id = random.randint(0, 9)
    policy_number = fake.random_int(min=1000, max=9999)
    expiry_date = fake.future_date(end_date="+5y")
    insurance_policies_data.append((policy_id, patient_id, company_id, policy_number, expiry_date))

# Generate fake data for Appointments table
appointments_data = []
for i in range(1000):
    appointment_id = i
    # Fetch valid doctor IDs from the doctors table
    cursor.execute("SELECT DoctorID FROM doctors")
    valid_doctor_ids = cursor.fetchall()
    # Choose a random valid doctor ID
    doctor_id = random.choice(valid_doctor_ids)[0]
    print(doctor_id)
    patient_id = random.randint(0, 999)
    appointment_date = fake.date_between(start_date="-1y", end_date="today")
    appointments_data.append((appointment_id, doctor_id, patient_id, appointment_date))

Insert the generated data into the database

print(patients_data)
# Insert patients data into Patients table
insert_patients_query = "INSERT INTO Patients (PatientID, FirstName, LastName, Gender, DateOfBirth, PhoneNumber, Address, City, State, Country, PostalCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_patients_query, patients_data)

# Insert doctors data into Doctors table
insert_doctors_query = "INSERT INTO Doctors (DoctorID, FirstName, LastName, Gender, DateOfBirth, PhoneNumber, Address, City, State, Country, PostalCode, Specialization) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_doctors_query, doctors_data)

# Insert medications data into Medications table
insert_medications_query = "INSERT INTO Medications (MedicationID,MedicationName) VALUES (%s, %s)"
cursor.executemany(insert_medications_query, medications_data)

# Insert lab tests data into LabTests table
insert_lab_tests_query = "INSERT INTO LabTests (TestID, TestName) VALUES (%s, %s)"
cursor.executemany(insert_lab_tests_query, lab_tests_data)

# Insert insurance companies data into InsuranceCompanies table
insert_insurance_companies_query = "INSERT INTO InsuranceCompanies (CompanyID, CompanyName, Address, City, State, Country, PostalCode) VALUES (%s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_insurance_companies_query, insurance_companies_data)

# Insert login data into Login table
insert_login_query = "INSERT INTO Login (UserID, Username, Password) VALUES (%s, %s, %s)"
cursor.executemany(insert_login_query, login_data)

# Insert appointments data into Appointments table
insert_appointments_query = "INSERT INTO Appointments (AppointmentID, DoctorID, PatientID, AppointmentDateTime) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_appointments_query, appointments_data)

# Insert prescriptions data into Prescriptions table
insert_prescriptions_query = "INSERT INTO Prescriptions (PrescriptionID, AppointmentID, PatientID, DoctorID, PrescriptionDate) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_prescriptions_query, prescriptions_data)


# Insert prescription medications data into PrescriptionMedications table
insert_prescription_medications_query = "INSERT INTO PrescriptionMedications (PrescriptionID, MedicationID, Dosage, Frequency) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_prescription_medications_query, prescription_medications_data)

# Insert payments data into Payments table
insert_payments_query = "INSERT INTO Payments (PaymentID, PatientID, Amount, PaymentDate) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_payments_query, payments_data)

# Insert medical records data into MedicalRecords table
insert_medical_records_query = "INSERT INTO MedicalRecords (RecordID, PatientID, DoctorID, AppointmentID, Diagnosis, Treatment) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_medical_records_query, medical_records_data)

# Insert lab results data into LabResults table
insert_lab_results_query = "INSERT INTO LabResults (ResultID, LabTestID, PatientID, Result) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_lab_results_query, lab_results_data)

# Insert insurance policies data into InsurancePolicies table
insert_insurance_policies_query = "INSERT INTO InsurancePolicies (PolicyID, PatientID, CompanyID, PolicyNumber, ExpiryDate) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_insurance_policies_query, insurance_policies_data)


# Commit the changes and close the database connection
connection.commit()
connection.close()