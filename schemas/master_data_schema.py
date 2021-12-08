from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base

'''DB Schema master_data'''


class MasterData(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(512), nullable=False)
    urusan_id = Column(Integer, ForeignKey('urusan.id'))  # Foreign Key
    satuan = Column(String(32), nullable=True)
    parent_id = Column(Integer, ForeignKey(
        'master_data.id'), index=True)

    # Relationship
    children = relationship("MasterData",
                            backref=backref('parent', remote_side=[id])
                            )
