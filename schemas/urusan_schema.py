from sqlalchemy import Integer, String, Column, Boolean, DateTime
from sqlalchemy.orm import relationship

from db.base_class import Base
from schemas.opd_urusan_schema import association_table

'''DB Schema urusan'''


class Urusan(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=True)
    kode = Column(String(16), nullable=True, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    # Relationship
    opds = relationship(
        "OPD",
        secondary=association_table,
        back_populates="urusans")
