class Courier(object):
    def __init__(self, client, courier_id, name):
        self.client = client
        self.type_name = 'ns1:CourierType'
        self.id = courier_id
        self.name = name

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            courier_id=soap_dict.get('CourierID', None),
            name=soap_dict.get('CourierName', None)
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.shipping_client.factory.create(self.type_name)
        suds_object.CourierID= self.id
        suds_object.CourierName = self.name
        return suds_object
