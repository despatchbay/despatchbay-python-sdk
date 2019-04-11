import recipient, sender, parcel


class Shipment(object):
    def __init__(self, client, shipment_id=None, shipment_document_id=None, collection_id=None,
                 service_id=None, parcels=None, client_reference=None, recipient_address=None,
                 is_followed=None, is_printed=None, is_despatched=None, is_delivered=None,
                 is_cancelled=None, labels_url=None):
        self.client = client
        self.type_name = 'ns1:ShipmentReturnType'
        self.shipment_id = shipment_id
        self.shipment_document_id = shipment_document_id
        self.collection_id = collection_id
        self.service_id = service_id
        self.parcels = parcels
        self.client_reference = client_reference
        self.is_followed = is_followed
        self.is_printed = is_printed
        self.is_despatched = is_despatched
        self.is_delivered = is_delivered
        self.is_cancelled = is_cancelled
        self.labels_url = labels_url

    @classmethod
    def from_dict(cls, client, **kwargs):
        parcel_array = []
        for parcel_item in kwargs.get('Parcels'):
            parcel_array.append(parcel.Parcel.from_dict(
                client,
                **client.dict(parcel_item)
            ))
        return cls(
            client=client,
            shipment_id=kwargs.get('ShipmentID'),
            shipment_document_id=kwargs.get('ShipmentDocumentID'),
            collection_id=kwargs.get('CollectionID'),
            service_id=kwargs.get('ServiceID'),
            parcels=parcel_array,
            client_reference=kwargs.get('ClientReference'),
            recipient_address=recipient.Recipient.from_dict(
                client,
                **client.dict(kwargs.get('RecipientAddress', None))
            ),
            is_followed=kwargs.get('IsFollowed'),
            is_printed=kwargs.get('IsPrinted'),
            is_despatched=kwargs.get('IsDespatched'),
            is_delivered=kwargs.get('IsDelivered'),
            is_cancelled=kwargs.get('IsCancelled'),
            labels_url=kwargs.get('LabelsURL', None)
        )

    # todo: decide if needed
    # todo: decide if needed
    # def to_soap_object(self):
    #     suds_object = self.client.factory.create(self.type_name)
    #     parcel_array = self.client.factory.create('ns1:ArrayOfParcelType')
    #     soap_parcel_list = []
    #     for item in self.parcels:
    #         soap_parcel_list.append(item.to_soap_object())
    #     parcel_array.item = soap_parcel_list
    #     parcel_array._arrayType = "urn:ParcelType[]"
    #     if isinstance(self.collection_date, str):
    #         collection_date = self.client.factory.create('CollectionDateType')
    #         collection_date.CollectionDate = self.collection_date
    #     else:
    #         collection_date = self.collection_date
    #     suds_object.ServiceID = self.service_id
    #     suds_object.Parcels = parcel_array
    #     suds_object.ClientReference = self.client_reference
    #     suds_object.CollectionDate = collection_date
    #     suds_object.SenderAddress = self.sender_address.to_soap_object()
    #     suds_object.RecipientAddress = self.recipient_address.to_soap_object()
    #     suds_object.FollowShipment = self.follow_shipment
    #     return suds_object
