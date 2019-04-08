class Sender(object):
    def __init__(self, client, name=None, telephone=None, email=None, address=None, address_id=None):
        self.client = client
        self.type_name = 'ns1:SenderAddressType'
        self.name = name
        self.telephone = telephone
        self.email = email
        self.address_id = address_id
        self.address = address

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
