from despatchbay.entities.collection_date import CollectionDate
from entity import Entity


class ShipmentRequest(Entity):
    SOAP_MAP = {
        'ServiceID': {
            'property': 'service_id',
            'type': 'string',
        },
        'Parcels': {
            'property': 'parcels',
            'type': 'entityArray',
            'soap_type': 'ns1:ArrayOfParcelType',
        },
        'ClientReference': {
            'property': 'client_reference',
            'type': 'string',
        },
        'CollectionDate': {
            'property': 'collection_date',
            'type': 'entity',
        },
        'RecipientAddress': {
            'property': 'recipient_address',
            'type': 'entity',
        },
        'SenderAddress': {
            'property': 'sender_address',
            'type': 'entity',
        },
        'FollowShipment': {
            'property': 'follow_shipment',
            'type': 'boolean',
        }
    }

    SOAP_TYPE = 'ns1:ShipmentRequestType'

    def __init__(self, client, service_id=None, parcels=None, client_reference=None, collection_date=None,
                 sender_address=None, recipient_address=None, follow_shipment=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self._despatchbay_client = client
        self.service_id = service_id
        self.parcels = parcels
        self.client_reference = client_reference
        self._collection_date = self.validate_collection_date_object(collection_date)
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.follow_shipment = follow_shipment

    def validate_collection_date_object(self, collection_date):
        if isinstance(collection_date, str):
            return CollectionDate(self._despatchbay_client, date=collection_date)
        else:
            return collection_date

    @property
    def collection_date(self):
        return self._collection_date

    @collection_date.setter
    def collection_date(self, collection_date):
        self._collection_date = self.validate_collection_date_object(collection_date)
