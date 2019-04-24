from entities import sender, courier, collection_date
from entities.entity import Entity


class Collection(Entity):

    SOAP_MAP = {
        "CollectionID": {
            "property": "collection_id",
            "type": "string"
        },
        "CollectionDocumentID": {
            "property": "document_id",
            "type": "string"
        },
        "CollectionType": {
            "property": "collection_type",
            "type": "string"
        },
        "CollectionDate": {
            "property": "date",
            "type": "string"
        },
        "SenderAddress": {
            "property": "sender_address",
            "type": "string"
        },
        "Courier": {
            "property": "collection_courier",
            "type": "string"
        },
        "LabelsURL": {
            "property": "labels_url",
            "type": "string"
        },
        "Manifest": {
            "property": "manifest_url",
            "type": "string"
        }
    }

    SOAP_TYPE = 'ns1:CollectionReturnType'

    def __init__(self, client, collection_id=None, document_id=None, collection_type=None, date=None,
                 sender_address=None, collection_courier=None, labels_url=None, manifest_url=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
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
