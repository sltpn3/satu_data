from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema master_data'''


class MasterData(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(512), nullable=False)
    urusan_id = Column(Integer, ForeignKey('urusan.id'))  # Foreign Key
    satuan = Column(Integer, ForeignKey('satuan.id'))
    parent_id = Column(Integer, ForeignKey(
        'master_data.id'), index=True)
    nasional = Column(Boolean, default=False)
    provinsi = Column(Boolean, default=False)
    kabupaten = Column(Boolean, default=False)
    kecamatan = Column(Boolean, default=False)
    # tahunan, semester, triwulan, bulanan, mingguan
    timeframe = Column(String(128), default='tahunan')
    is_active = Column(Boolean, default=True)
    validation_flow_id = Column(Integer, ForeignKey('validation_flow.id'))
    # value_as = Column(String(128)) # sum_of_child, formula, normal, etc

    # Relationship
    children = relationship("MasterData",
                            backref=backref('parent', remote_side=[id])
                            )
    validation_flow = relationship("ValidationFlow",
                                   back_populates="masters_data"
                                   )
