import sender, courier, collection_date


class Collection(object):
    def __init__(self, client, id=None, document_id=None, collection_type=None,
                 date=None, sender_address=None, courier=None, labels_url=None, manifest_url=None):
        self.client = client
        self.type_name = 'ns1:CollectionReturnType'
        self.id = id
        self.document_id = document_id
        self.collection_type=collection_type
        self.date=date
        self.sender_address=sender_address
        self.courier=courier
        self.labels_url=labels_url
        self.manifest_url=manifest_url

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            id=kwargs.get('CollectionID'),
            document_id=kwargs.get('CollectionDocumentID'),
            collection_type=kwargs.get('CollectionType'),
            date=collection_date.CollectionDate.from_dict(
                client,
                **client.dict(kwargs.get('CollectionDate'))
            ),
            sender_address=sender.Sender.from_dict(
                client,
                **client.dict(kwargs.get('SenderAddress', None))
            ),
            courier=courier.Courier.from_dict(
                client,
                **client.dict(kwargs.get('Courier', None))
            ),
            labels_url=kwargs.get('LabelsURL', None),
            manifest_url=kwargs.get('Manifest', None)
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.CollectionID = self.id
        suds_object.CollectionDocumentID = self.document_id
        suds_object.CollectionType = self.collection_type
        suds_object.CollectionDate = self.date
        suds_object.SenderAddress = self.sender_address
        suds_object.Courier = self.courier
        suds_object.LabelsURL = self.labels_url
        suds_object.Manifest = self.manifest_url
        return suds_object
