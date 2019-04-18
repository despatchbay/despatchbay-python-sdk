class AddressKey(object):
    def __init__(self, client, key, address):
        self.addressing_client = client.addressing_client
        self.type_name = 'ns1:AddressKeyType'
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

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.addressing_client.factory.create(self.type_name)
        suds_object.key = self.key
        suds_object.address = self.address
        return suds_object
