from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()



class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone_number= Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hospital_id = Column(Integer, nullable = False )
    department = Column(Integer, nullable = False )

    patients = relationship('Patient', back_populates='doctor')

    def __repr__(self):
        return f'<Doctor(id={self.id}, name={self.name}, age={self.age}, phone_number={self.phone_number}, email={self.email}, hospital_id={self.hospital_id}, department={self.department})>'
    

class Patient (Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False) 
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    adm_number = Column(String, nullable=False)
    ward_name = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)

    doctor = relationship('Doctor', back_populates='patients')

    def __repr__(self):
        return f'<Patient(id={self.id}, name={self.name}, age={self.age}, phone_number={self.phone_number}, email={self.email}, adm_number={self.adm_number}, ward_name={self.ward_name}, doctor_id={self.doctor_id})>'
    
