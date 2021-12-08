from sqlalchemy import Integer, String, Column, Boolean, DateTime
from sqlalchemy.orm import relationship

from db.base_class import Base

'''DB Schema urusan'''


class Urusan(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=True, unique=True)
