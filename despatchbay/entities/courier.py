from entity import Entity


class Courier(Entity):

    SOAP_MAP = {
        'CourierID': {
            'property': 'courier_id',
            'type': 'integer'
        },
        'CourierName': {
            'property': 'name',
            'type': 'string'
        }
    }
    SOAP_TYPE = 'ns1:CourierType'

    def __init__(self, client, courier_id=None, name=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.courier_id = courier_id
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
