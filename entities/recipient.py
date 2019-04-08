class Recipient(object):
    def __init__(self, client, name=None, telephone=None, email=None, address=None):
        self.client = client
        self.type_name = 'ns1:RecipientAddressType'
        self.name = name
        self.telephone = telephone
        self.email = email
        self.address = address

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.RecipientName = self.name
        suds_object.RecipientTelephone = self.telephone
        suds_object.RecipientEmail = self.email
        suds_object.RecipientAddress = self.address.to_soap_object()
        return suds_object
