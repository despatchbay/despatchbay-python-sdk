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

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            weight=kwargs.get('Weight', None),
            length=kwargs.get('Length', None),
            width=kwargs.get('Width', None),
            height=kwargs.get('Height', None),
            contents=kwargs.get('Contents', None),
            value=kwargs.get('Value', None),
            tracking_number=kwargs.get('TrackingNumber', None)
        )

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
