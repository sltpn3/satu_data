from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema validation_flow'''


class ValidationFlow(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True)
    status_start_id = Column(Integer, ForeignKey(
        'status.id'), index=True)
    is_active = Column(Boolean, default=True)

    # Relationship
    masters_data = relationship("MasterData", back_populates="validation_flow")
