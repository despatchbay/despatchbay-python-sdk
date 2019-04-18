class CollectionDate(object):
    def __init__(self, client, date=None):
        self.client = client
        self.type_name = 'ns1:CollectionDateType'
        self.date = date

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            date=soap_dict.get('CollectionDate', None)
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.shipping_client.factory.create(self.type_name)
        suds_object.CollectionDate = self.date
