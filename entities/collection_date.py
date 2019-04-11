class CollectionDate(object):
    def __init__(self, client, date=None):
        self.client = client
        self.type_name = 'ns1:CollectionDateType'
        self.date = date

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            date=kwargs.get('CollectionDate', None)
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.CollectionDate = self.date
