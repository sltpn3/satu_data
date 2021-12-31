from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema status_update'''


class StatusUpdate(Base):
    id = Column(Integer, primary_key=True, index=True)
    input_history_id = Column(Integer, ForeignKey(
        'input_history.id'), index=True)
    status_updated_to = Column(Integer, ForeignKey(
        'status.id'), index=True)
    status_updated_by = Column(Integer, ForeignKey(
        'user.id'), index=True)
    created_at = Column(DateTime)

    # Relationship
    input_history = relationship("InputHistory", back_populates="status_updates")
    updated_by = relationship("User", back_populates="status_updates")
    status = relationship("Status", back_populates="status_updates")