from entity import Entity


class Recipient(Entity):
    def __init__(self, client, name=None, telephone=None, email=None, address=None):

        Entity.__init__(self, client)

        self.type_name = 'ns1:RecipientAddressType'
        self.suds_object = self.client.factory.create(self.type_name)

        self.suds_object.RecipientName = name
        self.suds_object.RecipientTelephone = telephone
        self.suds_object.RecipientEmail = email
        self.suds_object.RecipientAddress = address.get_soap_object()

    def get_soap_object(self):
        return self.suds_object
