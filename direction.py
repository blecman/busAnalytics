from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('direction_id', Integer, ForeignKey('direction.id')),
    Column('stop_id', Integer, ForeignKey('stop.id'))
)

class Direction:

    __tablename__='direction'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    title = Column(String)

    stops = relationship("Stop",
                    secondary=association_table)

    def __init__(self, attrib):
        props = ['tag', 'title', 'stops']
        for prop in props:
            if prop in attrib:
                setattr(self, prop, attrib[prop])
            else:
                setattr(self, prop, None)

    def __repr__ (self):
        return "Direction (Tag: {}, Title: {}, StopList: {})".format(self.tag, self.title, self.stops)
