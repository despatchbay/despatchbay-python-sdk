from entity import Entity


class Sender(Entity):
    # todo: handle the exclusivity of senderaddress or senderaddressid
    def __init__(self, client, name=None, telephone=None, email=None, address=None, address_id=None):

        Entity.__init__(self, client)

        self.type_name = 'ns1:SenderAddressType'
        self.suds_object = self.client.factory.create(self.type_name)

        self.suds_object.SenderName = name
        self.suds_object.SenderTelephone = telephone
        self.suds_object.SenderEmail = email
        if address_id:
            self.suds_object.SenderAddressID = address_id
        else:
            self.suds_object.SenderAddress = address.get_soap_object()

    def get_soap_object(self):
        return self.suds_object
