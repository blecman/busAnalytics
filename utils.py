import json

class MyEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that leverages an object's `__json__()` method,
    if available, to obtain its default JSON representation.

    """
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)

def propsToDict(obj, props):
    d = {}
    for prop in props:
        d[prop] = getattr(obj, prop)
    return d

def toJson(obj):
    return json.dumps(obj, cls=MyEncoder)
