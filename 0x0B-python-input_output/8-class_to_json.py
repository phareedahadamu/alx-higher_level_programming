#!/usr/bin/python3
""" Defines the class_to_json function"""


def class_to_json(obj):
    """ A function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object"""

    import json
    from json import JSONEncoder

    class objEncoder(JSONEncoder):
        """ Defines a class objEncoder that encodes the class
        and converts to a dict"""
        def default(self, my_obj):
            """ converts to a dict"""
            return my_obj.__dict__
    objEncoder().encode(obj)
    objJSON = json.dumps(obj, cls=objEncoder)
    return json.loads(objJSON)
