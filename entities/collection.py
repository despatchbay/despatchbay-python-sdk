import sender, courier, collection_date


class Collection(object):
    def __init__(self, client, collection_id=None, document_id=None, collection_type=None, date=None,
                 sender_address=None, collection_courier=None, labels_url=None, manifest_url=None):
        self.client = client
        self.type_name = 'ns1:CollectionReturnType'
        self.collection_id = collection_id
        self.document_id = document_id
        self.collection_type = collection_type
        self.date = date
        self.sender_address = sender_address
        self.collection_courier = collection_courier
        self.labels_url = labels_url
        self.manifest_url = manifest_url

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            collection_id=soap_dict.get('CollectionID'),
            document_id=soap_dict.get('CollectionDocumentID'),
            collection_type=soap_dict.get('CollectionType'),
            date=collection_date.CollectionDate.from_dict(
                client,
                client.dict(soap_dict.get('CollectionDate'))
            ),
            sender_address=sender.Sender.from_dict(
                client,
                client.dict(soap_dict.get('SenderAddress', None))
            ),
            collection_courier=courier.Courier.from_dict(
                client,
                client.dict(soap_dict.get('Courier', None))
            ),
            labels_url=soap_dict.get('LabelsURL', None),
            manifest_url=soap_dict.get('Manifest', None)
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.shipping_client.factory.create(self.type_name)
        suds_object.CollectionID = self.collection_id
        suds_object.CollectionDocumentID = self.document_id
        suds_object.CollectionType = self.collection_type
        suds_object.CollectionDate = self.date
        suds_object.SenderAddress = self.sender_address
        suds_object.Courier = self.collection_courier
        suds_object.LabelsURL = self.labels_url
        suds_object.Manifest = self.manifest_url
        return suds_object
