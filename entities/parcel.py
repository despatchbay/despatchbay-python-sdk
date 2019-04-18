class Parcel(object):
    def __init__(self, client, weight=None, length=None, width=None, height=None,
                 contents=None, value=None, tracking_number=None):
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
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            weight=soap_dict.get('Weight', None),
            length=soap_dict.get('Length', None),
            width=soap_dict.get('Width', None),
            height=soap_dict.get('Height', None),
            contents=soap_dict.get('Contents', None),
            value=soap_dict.get('Value', None),
            tracking_number=soap_dict.get('TrackingNumber', None)
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.shipping_client.factory.create(self.type_name)
        suds_object.Weight = self.weight
        suds_object.Length = self.length
        suds_object.Width = self.width
        suds_object.Height = self.height
        suds_object.Contents = self.contents
        suds_object.Value = self.value
        suds_object.TrackingNumber = self.tracking_number
        return suds_object
