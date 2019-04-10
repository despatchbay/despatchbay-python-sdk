import address

class Sender(object):
    def __init__(self, client, name=None, telephone=None, email=None, address=None, address_id=None):
        self.client = client
        self.type_name = 'ns1:SenderAddressType'
        self.name = name
        self.telephone = telephone
        self.email = email
        self.address_id = address_id
        self.address = address

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            name=kwargs.get('SenderName', None),
            telephone=kwargs.get('SenderTelephone', None),
            email=kwargs.get('SenderEmail', None),
            address_id=kwargs.get('SenderAddressID'),
            address=address.Address.from_dict(
                client,
                **client.accounts_client.dict(kwargs.get('SenderAddress', None))
            )
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.SenderName = self.name
        suds_object.SenderTelephone = self.telephone
        suds_object.SenderEmail = self.email
        if self.address_id:
            suds_object.SenderAddressID = self.address_id
        else:
            suds_object.SenderAddress = self.address.to_soap_object()
        return suds_object
