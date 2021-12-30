from typing import Text
from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey, Date
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
    from_date = Column(Date)
    to_date = Column(Date)
    notes = Column(String(256))
    is_active = Column(Boolean, default=True)

    # Relationship
    input_histories = relationship("InputHistory", back_populates="input_data",
                                   order_by="asc(InputHistory.created_at)")
