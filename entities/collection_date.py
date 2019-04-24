from entities.entity import Entity


class CollectionDate(Entity):
    SOAP_MAP = {
        "CollectionDate": {
            "property": "date",
            "type": "string"
        }
    }

    SOAP_TYPE = 'ns1:CollectionDateType'

    def __init__(self, client, date=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
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
