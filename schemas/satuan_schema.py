from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema satuan'''


class Satuan(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(512), nullable=False)
    type = Column(Integer, ForeignKey('satuan_type.id'), nullable=False)
    is_active = Column(Boolean, default=True)
