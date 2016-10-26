import requests
from xml.etree import ElementTree

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from stop import Stop
import stop
from direction import Direction
from predictions import Predictions

Base = declarative_base()

class Route(Base):

    __tablename__='route'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    title = Column(String)

    agency_id = Column(Integer, ForeignKey('agency.id'))
    agency = relationship("Agency", back_populates="routes")

    stops = relationship("Stop", back_populates="route")
    directions = relationship("Direction", back_populates="route")

    def __init__(self, attrib):
        props = ['tag', 'title']
        for prop in props:
            setattr(self, prop, attrib[prop])

        self.getStopList()

    def getStopList(self):

        response = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a={}&r={}".format(self.agency.tag,self.tag))

        body = ElementTree.fromstring(response.content)
        routeTag = body.find('route')

        for stopTag in routeTag.findall('stop'):
            self.stops.append(Stop(stopTag.attrib))

    def getStop (self, tag):
        for aStop in self.stops:
            if aStop.tag == tag:
                return aStop
        return None

    def getDirectionList(self):
        self.directionList = []

        response = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a={}&r={}".format(self.agency.tag,self.tag))

        body = ElementTree.fromstring(response.content)
        routeTag = body.find('direction')

        for directionTag in routeTag.findall('direction'):
            attrib = directionTag.attrib

            attrib['stopList'] = []
            for stopTag in directionTag.findall('stop'):
                stop = self.get_stop(stopTag.attrib['tag'])
                if stop != None:
                    attrib['stopList'].append(stop)

            self.direction_list.append(Direction(attrib))

    def getPredictions(self):

        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a={}".format(self.agency.tag)

        for stop in self.stopList:
            url += "&stops={}|{}".format(self.tag,stop.tag)

        response = requests.get(url)

        body = ElementTree.fromstring(response.content)

        predictions = []
        for predictionsTag in body.findall('predictions'):
            predictions.append(Predictions(predictionsTag).toDict())
        return predictions

    def __repr__ (self):
        return "Route (Tag: {}, Title: {}, StopList: {})".format(self.tag, self.title, self.stopList)
