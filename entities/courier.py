class Courier(object):
    def __init__(self,client, id, name):
        self.client = client
        self.type_name = 'ns1:CourierType'
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            id=kwargs.get('CourierID', None),
            name=kwargs.get('CourierName', None)
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.CourierID= self.id
        suds_object.CourierName = self.name
        return suds_object
