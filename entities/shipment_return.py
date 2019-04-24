from entities import recipient
from entities import parcel


class ShipmentReturn(object):
    def __init__(self, client, shipment_id=None, shipment_document_id=None, collection_id=None,
                 service_id=None, parcels=None, client_reference=None, recipient_address=None,
                 is_followed=None, is_printed=None, is_despatched=None, is_delivered=None,
                 is_cancelled=None, labels_url=None):
        self.despatchbay_client = client
        self.shipping_client = client.shipping_client
        self.type_name = 'ns1:ShipmentReturnType'
        self.shipment_id = shipment_id
        self.shipment_document_id = shipment_document_id
        self.collection_id = collection_id
        self.service_id = service_id
        self.parcels = parcels
        self.client_reference = client_reference
        self.recipient_address = recipient_address
        self.is_followed = is_followed
        self.is_printed = is_printed
        self.is_despatched = is_despatched
        self.is_delivered = is_delivered
        self.is_cancelled = is_cancelled
        self.labels_url = labels_url

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        parcel_array = []
        for parcel_item in soap_dict.get('Parcels'):
            parcel_array.append(
                parcel.Parcel.from_dict(
                    client,
                    client.shipping_client.dict(parcel_item)
                )
            )
        return cls(
            client=client,
            shipment_id=soap_dict.get('ShipmentID'),
            shipment_document_id=soap_dict.get('ShipmentDocumentID'),
            collection_id=soap_dict.get('CollectionID'),
            service_id=soap_dict.get('ServiceID'),
            parcels=parcel_array,
            client_reference=soap_dict.get('ClientReference'),
            recipient_address=recipient.Recipient.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('RecipientAddress', None))
            ),
            is_followed=soap_dict.get('IsFollowed'),
            is_printed=soap_dict.get('IsPrinted'),
            is_despatched=soap_dict.get('IsDespatched'),
            is_delivered=soap_dict.get('IsDelivered'),
            is_cancelled=soap_dict.get('IsCancelled'),
            labels_url=soap_dict.get('LabelsURL', None)
        )

    def cancel(self):
        """
        Makes a CancelShipment request through the Despatch Bay API client.
        """
        cancel_return = self.despatchbay_client.cancel_shipment(self.shipment_id)
        if cancel_return:
            self.is_cancelled = True
        return cancel_return

    def get_labels(self, **kwargs):
        """
        Fetches label pdf through the Despatch Bay API client.
        """
        return self.despatchbay_client.fetch_shipment_labels(self.shipment_document_id, **kwargs)
