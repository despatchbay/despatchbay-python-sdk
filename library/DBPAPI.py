from suds.client import Client
from suds.transport.http import HttpAuthenticated


from entities.parcel import Parcel
from entities.address import Address
from entities.recipient import Recipient
from entities.sender import Sender
from entities.shipment_request import Shipment
from entities.account import Account
from entities.account_balance import AccountBalance
from entities.address_key import AddressKey
from entities.service import Service
from entities.collection import Collection
from entities.shipment_return import Shipment
from library.pdf_client import PdfClient


class DespatchBayAPI(object):

    def __init__(self, apiuser, apikey):
        url = 'http://api.despatchbay.st'
        soap_path = '/soap/%s/%s?wsdl'
        documents_path = '/documents/v1/'
        account_url = url + soap_path % ('v15', 'account')
        shipping_url = url + soap_path % ('v15', 'shipping')
        addressing_url = url + soap_path % ('v15', 'addressing')
        tracking_url = url + soap_path % ('v15', 'tracking')
        self.accounts_client = Client(
            account_url, transport=self.create_transport(apiuser, apikey))
        self.addressing_client = Client(
            addressing_url, transport=self.create_transport(apiuser, apikey))
        self.shipping_client = Client(
            shipping_url, transport=self.create_transport(apiuser, apikey))
        self.tracking_client = Client(
            tracking_url, transport=self.create_transport(apiuser, apikey))
        self.labels_url = url + documents_path + 'labels'
        self.manifest_url = url + documents_path + 'manifest'
        # todo set user agent
        self.pdf_client = PdfClient({'apiUser': apiuser, 'apikey': apikey}, 'some_user_agent')
        print(addressing_url)

    @staticmethod
    def create_transport(username, password):
        return HttpAuthenticated(username=username, password=password)

    # Shipping entities

    def parcel(self, **kwargs):
        """
        Creates a dbp parcel entity
        """
        return Parcel(self.shipping_client, **kwargs)

    def address(self, **kwargs):
        """
        Creates a dbp address entity
        """
        return Address(self.shipping_client, **kwargs)

    def recipient(self, **kwargs):
        """
        Creates a dbp recipient address entity
        """
        return Recipient(self.shipping_client, **kwargs)

    def sender(self, **kwargs):
        """
        Creates a dbp sender address entity
        """
        return Sender(self.shipping_client, **kwargs)

    def shipment(self, **kwargs):
        """
        Creates a dbp shipment entity
        """
        return Shipment(self.shipping_client, **kwargs)

    # Account Services

    def get_account(self):
        account_dict = self.accounts_client.dict(self.accounts_client.service.GetAccount())
        return Account.from_dict(
            self.accounts_client,
            **account_dict
        )

    def get_account_balance(self):
        balance_dict = self.accounts_client.dict(self.accounts_client.service.GetAccountBalance())
        return AccountBalance.from_dict(
            self.accounts_client,
            **balance_dict
        )

    def get_sender_addresses(self):
        sender_addresses_dict_list = []
        for sender_address in self.accounts_client.service.GetSenderAddresses():
            sender_address_dict = self.accounts_client.dict(sender_address)
            sender_addresses_dict_list.append(Sender.from_dict(
                self.accounts_client,
                **sender_address_dict))
        return sender_addresses_dict_list

    # Addressing Services

    def find_address(self, postcode, property_string):
        found_address_dict = self.addressing_client.dict(
            self.addressing_client.service.FindAddress(
                postcode, property_string
            ))
        return Address.from_dict(
            self.addressing_client,
            **found_address_dict
        )

    def get_address_by_key(self, key):
        found_address_dict = self.addressing_client.dict(
            self.addressing_client.service.GetAddressByKey(key)
        )
        return Address.from_dict(
            self.addressing_client,
            **found_address_dict
        )

    def get_address_keys_by_postcode(self, postcode):
        address_keys_dict_list = []
        for soap_address_key in self.addressing_client.service.GetAddressKeysByPostcode(postcode):
            address_key_dict = self.accounts_client.dict(soap_address_key)
            address_keys_dict_list.append(AddressKey.from_dict(
                self.addressing_client,
                **address_key_dict))
        return address_keys_dict_list

    # Shipping services

    def get_available_services(self, shipment_request):
        available_service_dict_list = []
        for available_service in self.shipping_client.service.GetAvailableServices(
                shipment_request.to_soap_object()):
            available_service_dict = self.shipping_client.dict(available_service)
            available_service_dict_list.append(Service.from_dict(
                self.shipping_client,
                **available_service_dict))
        return available_service_dict_list

    def get_available_collection_dates(self, sender_address, courier_id):
        available_collection_dates_response = self.shipping_client.service.GetAvailableCollectionDates(
            sender_address.to_soap_object(), courier_id)
        available_collection_dates_list = []
        for collection_date in available_collection_dates_response:
            collection_date_dict = self.shipping_client.dict(collection_date)
            available_collection_dates_list.append(collection_date_dict['CollectionDate'])
        return available_collection_dates_list

    def get_collection(self, collection_id):
        collection_dict = self.shipping_client.dict(
            self.shipping_client.service.GetCollection(collection_id))
        return Address.from_dict(
            self.shipping_client,
            **collection_dict
        )

    def get_collections(self):
        collections_dict_list = []
        for found_collection in self.shipping_client.service.GetCollections():
            collection_dict = self.shipping_client.dict(found_collection)
            collections_dict_list.append(
                Collection.from_dict(
                    self.shipping_client,
                    **collection_dict
                )
            )
        return collections_dict_list

    def get_shipment(self, shipment_id):
        shipment_dict = self.shipping_client.dict(
            self.shipping_client.service.GetShipment(shipment_id))
        return Shipment.from_dict(
            self.shipping_client,
            **shipment_dict
        )

    def add_shipment(self, shipment_request):
        return self.shipping_client.service.AddShipment(shipment_request.to_soap_object())

    def book_shipments(self, shipment_ids):
        array_of_shipment_id = self.shipping_client.factory.create('ns1:ArrayOfShipmentID')
        array_of_shipment_id.item = shipment_ids
        booked_shipments_list = []
        for booked_shipment in self.shipping_client.service.BookShipments(array_of_shipment_id):
            booked_shipment_dict = self.shipping_client.dict(booked_shipment)
            booked_shipments_list.append(
                Shipment.from_dict(
                    self.shipping_client,
                    **booked_shipment_dict
                )
            )
        return booked_shipments_list

    def cancel_shipment(self, shipment_id):
        return self.shipping_client.service.CancelShipment(shipment_id)

    # Tracking services

    def get_tracking(self, tracking_number):
        return self.tracking_client.service.GetTracking(tracking_number)

    # Labels services

    def fetch_shipment_labels(self, document_id, **kwargs):
        self.pdf_client.fetch_shipment_labels(document_id, **kwargs)

    def fetch_manifest(self, collection_id):
        self.pdf_client.fetch_manifest(collection_id)
