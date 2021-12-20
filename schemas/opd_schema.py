from sqlalchemy import Integer, String, Column, Boolean, DateTime
from sqlalchemy.orm import relationship

from db.base_class import Base
from schemas.opd_urusan_schema import association_table

'''DB Schema OPD'''


class OPD(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=True)
    kode = Column(String(16), nullable=True, unique=True, index=True)

    # Relationship
    users = relationship("User", back_populates="organisasi")
    urusans = relationship(
        "Urusan",
        secondary=association_table,
        back_populates="opds")
