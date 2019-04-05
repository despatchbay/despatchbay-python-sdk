import xml.etree.ElementTree as ET


class Entity(object):

    def __init__(self, client):
        self.soap_map = None
        self.type_name = None
        self.client = client

