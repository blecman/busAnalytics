import utils, time
from prediction import Prediction

class Predictions:

    def __init__(self, predictionsTag):
        props = ['routeTitle', 'routeTag', 'stopTitle', 'stopTag']
        for prop in props:
            if prop in predictionsTag.attrib:
                setattr(self, prop, predictionsTag.attrib[prop])
            else:
                setattr(self, prop, None)

        self.getPredictionList(predictionsTag)

    def getPredictionList(self, predictionsTag):
        self.predictionList = []

        for directionTag in predictionsTag.findall('direction'):
            for predictionTag in directionTag.findall('prediction'):
                predictionTag.attrib['direction'] = directionTag.attrib['title']
                self.predictionList.append(Prediction(predictionTag.attrib))

    def __repr__ (self):
        props = ['routeTitle', 'routeTag', 'stopTitle', 'stopTag', 'predictionList']
        output = " Predictions("
        for prop in props:
            output += " {}: {}".format(prop, getattr(self, prop))
        return output + ")"

    def toDict (self):
        props = ['routeTitle', 'routeTag', 'stopTitle', 'stopTag']
        d = utils.propsToDict(self, props)

        d['predictionList'] = []
        for prediction in self.predictionList:
            d['predictionList'].append(prediction.toDict())
        d['time'] = time.time()
        return d
