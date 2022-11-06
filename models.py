from database import Base
from sqlalchemy import Column,String,Integer

"""_summary_
    
    class student:
        name:str
        age:int
        reg_no:text
        
    
"""

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
    def __repr__(self):
        return f'<Student {self.name}>'
    
    
    
    