from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema input_history'''


class InputHistory(Base):
    id = Column(Integer, primary_key=True, index=True)
    input_data_id = Column(Integer, ForeignKey(
        'input_data.id'), index=True)
    created_by = Column(Integer, ForeignKey(
        'user.id'), index=True)
    value = Column(Integer)
    revision = Column(Integer)
    created_at = Column(DateTime)

    # Relationship
    input_data = relationship("InputData", back_populates="input_histories")
    user = relationship("User", back_populates="input_histories")
    status_updates = relationship("StatusUpdate", back_populates="input_history")