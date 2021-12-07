from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema input_data'''


class InputData(Base):
    id = Column(Integer, primary_key=True, index=True)
    master_id = Column(Integer, ForeignKey(
        'master_data.id'), index=True)
    created_by = Column(Integer, ForeignKey(
        'user.id'), index=True)
    year = Column(Integer)