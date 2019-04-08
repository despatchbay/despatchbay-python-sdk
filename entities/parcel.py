class Parcel(object):
    def __init__(self, client, weight=None, length=None, width=None, height=None, contents=None, value=None, tracking_number=None):
        self.client = client
        self.type_name = 'ns1:ParcelType'
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.contents = contents
        self.value = value
        self.tracking_number = tracking_number

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.Weight = self.weight
        suds_object.Length = self.length
        suds_object.Width = self.width
        suds_object.Height = self.height
        suds_object.Contents = self.contents
        suds_object.Value = self.value
        suds_object.TrackingNumber = self.tracking_number
        return suds_object
