import address


class Recipient(object):
    def __init__(self, client, name=None, telephone=None, email=None, address=None):
        self.client = client
        self.type_name = 'ns1:RecipientAddressType'
        self.name = name
        self.telephone = telephone
        self.email = email
        self.address = address

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            name=kwargs.get('RecipientName', None),
            telephone=kwargs.get('RecipientTelephone', None),
            email=kwargs.get('RecipientEmail', None),
            address=address.Address.from_dict(
                client,
                **client.accounts_client.dict(kwargs.get('RecipientAddress', None))
            )
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.RecipientName = self.name
        suds_object.RecipientTelephone = self.telephone
        suds_object.RecipientEmail = self.email
        suds_object.RecipientAddress = self.address.to_soap_object()
        return suds_object
