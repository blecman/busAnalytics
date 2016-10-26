from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stop(Base):
    __tablename__='stop'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    title = Column(String)
    lat = Column(String)
    lon = Column(String)
    stopId = Column(String)

    route_id = Column(Integer, ForeignKey('route.id'))
    route = relationship("Route", back_populates="stops")

    def __init__ (self, attrib):
        props = ['tag', 'title', 'lat', 'lon', 'stopId']
        for prop in props:
            if prop in attrib:
                setattr(self, prop, attrib[prop])
            else:
                 setattr(self, prop, None)

    def __repr__ (self):
        return "Stop (Tag: {}, Title: {}, StopId: {})".format(self.tag, self.title, self.stopId)
