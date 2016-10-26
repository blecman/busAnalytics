import utils
class Prediction:

    def __init__ (self, attrib):
        props = ['epochTime', 'seconds', 'minutes', 'isDeparture', 'affectedByLayover', 'dirTag', 'vehicle', 'block', 'direction']

        for prop in props:
            if prop in attrib:
                setattr(self, prop, attrib[prop])
            else:
                setattr(self, prop, None)

    def __repr__ (self):
        props = ['epochTime', 'seconds', 'minutes', 'isDeparture', 'affectedByLayover', 'dirTag', 'vehicle', 'block', 'direction']
        output = "Prediction("
        for prop in props:
            output += " {}: {}".format(prop, getattr(self, prop))
        return output + ")"

    def toDict(self):
        props = ['epochTime', 'seconds', 'minutes', 'isDeparture', 'affectedByLayover', 'dirTag', 'vehicle', 'block', 'direction']
        return utils.propsToDict(self, props)
