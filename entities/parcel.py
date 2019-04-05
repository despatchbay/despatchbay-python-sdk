from entity import Entity


class Parcel(Entity):
    def __init__(self, client, weight=None, length=None, width=None, height=None, contents=None, value=None, tracking_number=None):

        Entity.__init__(self, client)

        self.type_name = 'ns1:ParcelType'
        self.suds_object = self.client.factory.create(self.type_name)

        self.suds_object.Weight = weight
        self.suds_object.Length = length
        self.suds_object.Width = width
        self.suds_object.Height = height
        self.suds_object.Contents = contents
        self.suds_object.Value = value
        self.suds_object.TrackingNumber = tracking_number

    def get_soap_object(self):
        return self.suds_object
