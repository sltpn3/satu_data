from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from db.base_class import Base

'''Relationship Schema between opd and urusan'''


association_table = Table('opd_urusan', Base.metadata,
                          Column('opd_id', ForeignKey(
                              'opd.id'), primary_key=True),
                          Column('urusan_id', ForeignKey(
                              'urusan.id'), primary_key=True)
                          )
