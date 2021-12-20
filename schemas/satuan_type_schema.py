from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema satuan_type'''


class SatuanType(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(512), nullable=False)
    store_column = Column(String(32), nullable=False)
    is_active = Column(Boolean, default=True)

    # Relationship
    satuans = relationship("Satuan", back_populates="tipe", uselist=True)
