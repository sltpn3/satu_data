from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

'''DB Schema user'''


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), index=True, unique=True)
    name = Column(String(128), nullable=True, unique=True)
    password = Column(String(32))
    opd_id = Column(Integer, ForeignKey('opd.id'))  # Foreign Key
    role_id = Column(Integer, ForeignKey('role.id'))  # Foreign Key

    # Relationship
    organisasi = relationship("OPD", back_populates="users")
    role = relationship("Role", back_populates="users")
