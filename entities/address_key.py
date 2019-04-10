class AddressKey(object):
    def __init__(self, client, key, address):
        self.client = client
        self.type_name = 'ns1:AddressKeyType'
        self.key = key
        self.address = address

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            key=kwargs.get('Key', None),
            address=kwargs.get('Address', None)
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.key = self.key
        suds_object.address = self.address
        return suds_object
