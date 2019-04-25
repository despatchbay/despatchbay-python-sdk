from despatchbay.entities import address


class Sender(object):
    def __init__(self, client, name=None, telephone=None, email=None, sender_address=None, address_id=None):
        self.client = client
        self.type_name = 'ns1:SenderAddressType'
        self.name = name
        self.telephone = telephone
        self.email = email
        self.address_id = address_id
        self.sender_address = sender_address

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            name=soap_dict.get('SenderName', None),
            telephone=soap_dict.get('SenderTelephone', None),
            email=soap_dict.get('SenderEmail', None),
            address_id=soap_dict.get('SenderAddressID'),
            sender_address=address.Address.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('SenderAddress', None))
            )
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.shipping_client.factory.create(self.type_name)
        suds_object.SenderName = self.name
        suds_object.SenderTelephone = self.telephone
        suds_object.SenderEmail = self.email
        if self.address_id:
            suds_object.SenderAddressID = self.address_id
        else:
            suds_object.SenderAddress = self.sender_address.to_soap_object()
        return suds_object
