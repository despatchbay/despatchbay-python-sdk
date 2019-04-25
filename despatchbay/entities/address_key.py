from entity import Entity


class AddressKey(Entity):
    SOAP_MAP = {
        'Key': {
            'property': 'key',
            'type': 'string',
        },
        'Address': {
            'property': 'address',
            'type': 'string',
        }
    }
    SOAP_TYPE = 'ns1:AddressKeyType'

    def __init__(self, client, key, address):
        super().__init__(self.SOAP_TYPE, client, self.SOAP_MAP)
        self.key = key
        self.address = address

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            key=soap_dict.get('Key', None),
            address=soap_dict.get('Address', None)
        )
