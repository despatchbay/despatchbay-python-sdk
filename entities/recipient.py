from entities import address


class Recipient(object):
    def __init__(self, client, name=None, telephone=None, email=None, recipient_address=None):
        self.shipping_client = client.shipping_client
        self.type_name = 'ns1:RecipientAddressType'
        self.name = name
        self.telephone = telephone
        self.email = email
        self.recipient_address = recipient_address

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            name=soap_dict.get('RecipientName', None),
            telephone=soap_dict.get('RecipientTelephone', None),
            email=soap_dict.get('RecipientEmail', None),
            recipient_address=address.Address.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('RecipientAddress', None))
            )
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.shipping_client.factory.create(self.type_name)
        suds_object.RecipientName = self.name
        suds_object.RecipientTelephone = self.telephone
        suds_object.RecipientEmail = self.email
        suds_object.RecipientAddress = self.recipient_address.to_soap_object()
        return suds_object
