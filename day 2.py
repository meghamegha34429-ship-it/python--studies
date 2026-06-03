# gmail registration
def get_details():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email ID: ")
    return name, phone, email

def print_details(name, phone, email):
    print("\nGmail Registration Details")
    print("Name:", name)
    print("Phone:", phone)
    print("Email:", email)

name, phone, email = get_details()
print_details(name, phone, email)

# aadhaar_registration
def get_details():
    name = input("Enter Name: ")
    aadhaar = input("Enter Aadhaar Number: ")
    mobile = input("Enter Mobile Number: ")
    return name, aadhaar, mobile

def print_details(name, aadhaar, mobile):
    print("\nAadhaar Registration Details")
    print("Name:", name)
    print("Aadhaar Number:", aadhaar)
    print("Mobile:", mobile)

name, aadhaar, mobile = get_details()
print_details(name, aadhaar, mobile)

# college admission
def get_details():
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    department = input("Enter Department: ")
    return student_name, course, department

def print_details(student_name, course, department):
    print("\nCollege Admission Details")
    print("Student Name:", student_name)
    print("Course:", course)
    print("Department:", department)

student_name, course, department = get_details()
print_details(student_name, course, department)

# flight booking
def get_details():
    passenger_name = input("Enter Passenger Name: ")
    source = input("Enter Source City: ")
    destination = input("Enter Destination City: ")
    return passenger_name, source, destination

def print_details(passenger_name, source, destination):
    print("\nFlight Booking Details")
    print("Passenger Name:", passenger_name)
    print("Source:", source)
    print("Destination:", destination)

passenger_name, source, destination = get_details()
print_details(passenger_name, source, destination)

# hospital registration
def get_details():
    patient_name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    blood_group = input("Enter Blood Group: ")
    return patient_name, age, blood_group

def print_details(patient_name, age, blood_group):
    print("\nHospital Registration Details")
    print("Patient Name:", patient_name)
    print("Age:", age)
    print("Blood Group:", blood_group)

patient_name, age, blood_group = get_details()
print_details(patient_name, age, blood_group)
