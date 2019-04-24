from entities.entity import Entity


class Parcel(Entity):

    SOAP_MAP = {
        'Weight': {
            'property': 'weight',
            'type': 'float'
        },
        'Length': {
            'property': 'length',
            'type': 'float'
        },
        'Width': {
            'property': 'width',
            'type': 'float'
        },
        'Height': {
            'property': 'height',
            'type': 'float'
        },
        'Contents': {
            'property': 'contents',
            'type': 'string'
        },
        'Value': {
            'property': 'value',
            'type': 'float'
        },
        'TrackingNumber': {
            'property': 'tracking_number',
            'type': 'string'
        }
    }
    SOAP_TYPE = 'ns1:ParcelType'

    def __init__(self, client, weight=None, length=None, width=None, height=None,
                 contents=None, value=None, tracking_number=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.client = client
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
