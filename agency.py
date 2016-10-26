import requests
from xml.etree import ElementTree

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from route import Route

Base = declarative_base()

class Agency(Base):
    __tablename__='agency'

    id = Column(Integer, primary_key=True)
    tag = Column(String)

    routes = relationship("Route", back_populates="agency")

    def __init__ (self, tag):
        self.tag = tag
        self.getRouteList()

    def getRouteList(self):

        response = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a={}".format(self.tag))

        body = ElementTree.fromstring(response.content)

        for routeTag in body:
            routeTag.attrib['agencyTag'] = self.tag

            self.routes.append(route.Route(routeTag.attrib))

    def getRoute(self, tag):
        for aRoute in self.routes:
            if aRoute.tag == tag:
                return aRoute
        return None
