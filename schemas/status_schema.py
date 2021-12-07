from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema status'''


class Status(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=True, unique=True)
    role_in_process = Column(Integer, ForeignKey('role.id'))  # Foreign Key
    parent_id = Column(Integer, ForeignKey(
        'status.id'), index=True)

    # Relationship
    children = relationship("Status",
                            backref=backref('parent', remote_side=[id])
                            )
