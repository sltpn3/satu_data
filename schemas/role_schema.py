from sqlalchemy import Integer, String, Column, Boolean, DateTime
from sqlalchemy.orm import relationship

from db.base_class import Base

'''DB Schema role'''


class Role(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=True, unique=True)
    is_active = Column(Boolean, default=True)

    # Relationship
    users = relationship("User", back_populates="role")
