from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    admission_date = Column(Date)
    exit_date = Column(Date)
    fees_paid = Column(Integer)
    fees_balance = Column(Integer)
    aadhar_number = Column(String)
    dob = Column(Date)
    place_of_birth = Column(String)
    unique_id = Column(String)

Base.metadata.create_all(engine)

# Function to add a student
def add_student():
    # Code to add student
    pass

# Function to view all students
def view_students():
    # Code to view all students
    pass

# Function to update a student
def update_student():
    # Code to update student
    pass

# Function to delete a student
def delete_student():
    # Code to delete student
    pass



def add_student():
    name = input("Enter student name: ")
    admission_date = input("Enter admission date (YYYY-MM-DD): ")
    exit_date = input("Enter exit date (YYYY-MM-DD): ")
    fees_paid = int(input("Enter fees paid: "))
    fees_balance = int(input("Enter fees balance: "))
    aadhar_number = input("Enter Aadhar card number: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    place_of_birth = input("Enter place of birth: ")
    unique_id = input("Enter unique ID: ")

    new_student = Student(
        name=name,
        admission_date=admission_date,
        exit_date=exit_date,
        fees_paid=fees_paid,
        fees_balance=fees_balance,
        aadhar_number=aadhar_number,
        dob=dob,
        place_of_birth=place_of_birth,
        unique_id=unique_id
    )

    session.add(new_student)
    session.commit()
    print("Student added successfully!")


def view_students():
    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Admission Date: {student.admission_date}, Exit Date: {student.exit_date}, Fees Paid: {student.fees_paid}, Fees Balance: {student.fees_balance}, Aadhar Number: {student.aadhar_number}, DOB: {student.dob}, Place of Birth: {student.place_of_birth}, Unique ID: {student.unique_id}")



def update_student():
    student_id = int(input("Enter the student ID to update: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = input(f"New name (current: {student.name}): ") or student.name
        student.admission_date = input(f"New admission date (current: {student.admission_date}): ") or student.admission_date
        student.exit_date = input(f"New exit date (current: {student.exit_date}): ") or student.exit_date
        student.fees_paid = int(input(f"New fees paid (current: {student.fees_paid}): ") or student.fees_paid)
        student.fees_balance = int(input(f"New fees balance (current: {student.fees_balance}): ") or student.fees_balance)
        student.aadhar_number = input(f"New Aadhar number (current: {student.aadhar_number}): ") or student.aadhar_number
        student.dob = input(f"New DOB (current: {student.dob}): ") or student.dob
        student.place_of_birth = input(f"New place of birth (current: {student.place_of_birth}): ") or student.place_of_birth
        student.unique_id = input(f"New unique ID (current: {student.unique_id}): ") or student.unique_id

        session.commit()
        print("Student updated successfully!")
    else:
        print("Student not found.")



def delete_student():
    student_id = int(input("Enter the student ID to delete: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")



def add_student():
    print("Inside add_student function")
    # Rest of the code...

def view_students():
    print("Inside view_students function")
    # Rest of the code...

def update_student():
    print("Inside update_student function")
    # Rest of the code...

def delete_student():
    print("Inside delete_student function")
    # Rest of the code...



def add_student():
    print("Adding a new student:")
    name = input("Enter student name: ")
    admission_date = input("Enter admission date (YYYY-MM-DD): ")
    exit_date = input("Enter exit date (YYYY-MM-DD): ")
    fees_paid = int(input("Enter fees paid: "))
    fees_balance = int(input("Enter fees balance: "))
    aadhar_number = input("Enter Aadhar card number: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    place_of_birth = input("Enter place of birth: ")
    unique_id = input("Enter unique ID: ")

    new_student = Student(
        name=name,
        admission_date=admission_date,
        exit_date=exit_date,
        fees_paid=fees_paid,
        fees_balance=fees_balance,
        aadhar_number=aadhar_number,
        dob=dob,
        place_of_birth=place_of_birth,
        unique_id=unique_id
    )

    session.add(new_student)
    session.commit()
    print("Student added successfully!")



def view_students():
    print("Viewing all students:")
    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Admission Date: {student.admission_date}, Exit Date: {student.exit_date}, Fees Paid: {student.fees_paid}, Fees Balance: {student.fees_balance}, Aadhar Number: {student.aadhar_number}, DOB: {student.dob}, Place of Birth: {student.place_of_birth}, Unique ID: {student.unique_id}")



def update_student():
    print("Updating student information:")
    student_id = int(input("Enter the student ID to update: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = input(f"New name (current: {student.name}): ") or student.name
        student.admission_date = input(f"New admission date (current: {student.admission_date}): ") or student.admission_date
        student.exit_date = input(f"New exit date (current: {student.exit_date}): ") or student.exit_date
        student.fees_paid = int(input(f"New fees paid (current: {student.fees_paid}): ") or student.fees_paid)
        student.fees_balance = int(input(f"New fees balance (current: {student.fees_balance}): ") or student.fees_balance)
        student.aadhar_number = input(f"New Aadhar number (current: {student.aadhar_number}): ") or student.aadhar_number
        student.dob = input(f"New DOB (current: {student.dob}): ") or student.dob
        student.place_of_birth = input(f"New place of birth (current: {student.place_of_birth}): ") or student.place_of_birth
        student.unique_id = input(f"New unique ID (current: {student.unique_id}): ") or student.unique_id

        session.commit()
        print("Student updated successfully!")
    else:
        print("Student not found.")



def delete_student():
    print("Deleting a student:")
    student_id = int(input("Enter the student ID to delete: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")



from sqlalchemy.exc import SQLAlchemyError

def add_student():
    try:
        # existing code...
        session.add(new_student)
        session.commit()
        print("Student added successfully!")
    except SQLAlchemyError as e:
        print(f"Error adding student: {e}")
        session.rollback()



def add_student():
    try:
        # Collect data
        admission_date = input("Enter admission date (YYYY-MM-DD): ")
        # Validate date format
        from datetime import datetime
        try:
            datetime.strptime(admission_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        # Continue with adding student...



def add_student():
    """
    Adds a new student to the database.
    Collects input data and saves it.
    """
    # existing code...

