from sqlalchemy import Column, Integer, String, Date, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    admission_date = Column(Date, nullable=False)
    exit_date = Column(Date, nullable=True)
    fees_paid = Column(Float, nullable=False)
    fees_balance = Column(Float, nullable=False)
    aadhar_card_number = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    place_of_birth = Column(String, nullable=False)
    unique_id = Column(String, unique=True, nullable=False)

def get_engine():
    return create_engine('sqlite:///vaishnavi_school.db')

def get_session():
    engine = get_engine()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()



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
