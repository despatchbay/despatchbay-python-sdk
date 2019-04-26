from suds.client import Client
from suds.transport.http import HttpAuthenticated
import suds
from despatchbay.exceptions import AuthorizationException,\
    ApiException, ConnectionException, RateLimitException
from . import entities, documents_client


def handle_suds_fault(error):
    exception_info = error.args[0]
    if 'Unauthorized' in exception_info:
        raise AuthorizationException('Invalid API credentials') from error
    elif 'Could not connect to host' in exception_info:
        raise ConnectionException('Failed to connect to the Despatch Bay API') from error
    elif 'Your access rate limit for this service has been exceeded' in exception_info:
        raise RateLimitException(exception_info)
    else:
        raise ApiException(error) from error


def try_except(fn):
    """
    A decorator to catch suds exceptions
    """
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except suds.WebFault as detail:
            handle_suds_fault(detail)
    return wrapped


class DespatchBaySDK(object):

    def __init__(self, api_user, api_key, api_domain='api.despatchbay.com', api_version='15'):
        soap_url_template = 'http://{}/soap/v{}/{}?wsdl'
        documents_url = 'http://{}/documents/v1'.format(api_domain)
        account_url = soap_url_template.format(api_domain, api_version, 'account')
        shipping_url = soap_url_template.format(api_domain, api_version, 'shipping')
        addressing_url = soap_url_template.format(api_domain, api_version, 'addressing')
        tracking_url = soap_url_template.format(api_domain, api_version, 'tracking')
        self.account_client = Client(
            account_url, transport=self.create_transport(api_user, api_key))
        self.addressing_client = Client(
            addressing_url, transport=self.create_transport(api_user, api_key))
        self.shipping_client = Client(
            shipping_url, transport=self.create_transport(api_user, api_key))
        self.tracking_client = Client(
            tracking_url, transport=self.create_transport(api_user, api_key))
        self.pdf_client = documents_client.DocumentsClient(api_url=documents_url)

    @staticmethod
    def create_transport(username, password):
        return HttpAuthenticated(username=username, password=password)

    # Shipping entities

    def parcel(self, **kwargs):
        """
        Creates a dbp parcel entity
        """
        return entities.Parcel(self, **kwargs)

    def address(self, **kwargs):
        """
        Creates a dbp address entity
        """
        return entities.Address(self, **kwargs)

    def recipient(self, **kwargs):
        """
        Creates a dbp recipient address entity
        """
        return entities.Recipient(self, **kwargs)

    def sender(self, **kwargs):
        """
        Creates a dbp sender address entity
        """
        return entities.Sender(self, **kwargs)

    def shipment_request(self, **kwargs):
        """
        Creates a dbp shipment entity
        """
        return entities.ShipmentRequest(self, **kwargs)

    # Account Services

    @try_except
    def get_account(self):
        """Calls GetAccount from the Despatch Bay Account Service."""
        account_dict = self.account_client.dict(self.account_client.service.GetAccount())
        return entities.Account.from_dict(
            self,
            account_dict
        )

    @try_except
    def get_account_balance(self):
        """
        Calls GetBalance from the Despatch Bay Account Service.
        """
        balance_dict = self.account_client.dict(self.account_client.service.GetAccountBalance())
        return entities.AccountBalance.from_dict(
            self,
            balance_dict
        )

    @try_except
    def get_sender_addresses(self):
        """
        Calls GetSenderAddresses from the Despatch Bay Account Service.
        """
        sender_addresses_dict_list = []
        for sender_address in self.account_client.service.GetSenderAddresses():
            sender_address_dict = self.account_client.dict(sender_address)
            sender_addresses_dict_list.append(entities.Sender.from_dict(
                self,
                sender_address_dict))
        return sender_addresses_dict_list

    @try_except
    def get_services(self):
        """
        Calls GetServices from the Despatch Bay Account Service.
        """
        service_list = []
        for account_service in self.account_client.service.GetServices():
            service_list.append(
                entities.Service.from_dict(
                    self,
                    self.account_client.dict(account_service)
                ))
        return service_list

    @try_except
    def get_payment_methods(self):
        """
        Calls GetPaymentMethods from the Despatch Bay Account Service.
        """
        payment_methods = []
        for payment_method in self.account_client.service.GetPaymentMethods():
            payment_methods.append(
                entities.PaymentMethod.from_dict(
                    self,
                    self.account_client.dict(payment_method)
                )
            )
        return payment_methods

    @try_except
    def enable_automatic_topups(self, minimum_balance=None, topup_amount=None,
                                payment_method_id=None, automatic_topup_settings_object=None):
        """
        Calls EnableAutomaticTopups from the Despatch Bay Account Service.

        Passing an automatic_topup_settings object takes priority over using individual arguments.
        """
        if not automatic_topup_settings_object:
            automatic_topup_settings_object = entities.AutomaticTopupSettings(
                self, minimum_balance, topup_amount, payment_method_id)
        return self.account_client.service.EnableAutomaticTopups(
            automatic_topup_settings_object.to_soap_object())

    @try_except
    def disable_automatic_topups(self):
        """
        Calls DisableAutomaticTopups from the Despatch Bay Account Service.
        """
        return self.account_client.service.DisableAutomaticTopups()

    # Addressing Services

    @try_except
    def find_address(self, postcode, property_string):
        """
        Calls FindAddress from the Despatch Bay Addressing Service.
        """
        found_address_dict = self.addressing_client.dict(
            self.addressing_client.service.FindAddress(
                postcode, property_string
            ))
        return entities.Address.from_dict(
            self,
            found_address_dict
        )

    @try_except
    def get_address_by_key(self, key):
        """
        Calls GetAddressByKey from the Despatch Bay Addressing Service.
        """
        found_address_dict = self.addressing_client.dict(
            self.addressing_client.service.GetAddressByKey(key)
        )
        return entities.Address.from_dict(
            self,
            found_address_dict
        )

    @try_except
    def get_address_keys_by_postcode(self, postcode):
        """
        Calls GetAddressKeysFromPostcode from the Despatch Bay Addressing Service.
        """
        address_keys_dict_list = []
        for soap_address_key in self.addressing_client.service.GetAddressKeysByPostcode(postcode):
            address_key_dict = self.account_client.dict(soap_address_key)
            address_keys_dict_list.append(entities.AddressKey.from_dict(
                self,
                address_key_dict))
        return address_keys_dict_list

    # Shipping services

    @try_except
    def get_available_services(self, shipment_request):
        """
        Calls GetAvailableServices from the Despatch Bay Shipping Service.
        """
        available_service_dict_list = []
        for available_service in self.shipping_client.service.GetAvailableServices(
                shipment_request.to_soap_object()):
            available_service_dict = self.shipping_client.dict(available_service)
            available_service_dict_list.append(entities.Service.from_dict(
                self,
                available_service_dict))
        return available_service_dict_list

    @try_except
    def get_available_collection_dates(self, sender_address, courier_id):
        """
        Calls GetAvailableCollectionDates from the Despatch Bay Shipping Service.
        """
        available_collection_dates_response = self.shipping_client.service.GetAvailableCollectionDates(
            sender_address.to_soap_object(), courier_id)
        available_collection_dates_list = []
        for collection_date in available_collection_dates_response:
            collection_date_dict = self.shipping_client.dict(collection_date)
            available_collection_dates_list.append(entities.CollectionDate.from_dict(self, collection_date_dict))
        return available_collection_dates_list

    @try_except
    def get_collection(self, collection_id):
        """
        Calls GetCollection from the Despatch Bay Shipping Service.
        """
        collection_dict = self.shipping_client.dict(
            self.shipping_client.service.GetCollection(collection_id))
        return entities.Address.from_dict(
            self,
            collection_dict
        )

    @try_except
    def get_collections(self):
        """
        Calls GetCollections from the Despatch Bay Shipping Service.
        """
        collections_dict_list = []
        for found_collection in self.shipping_client.service.GetCollections():
            collection_dict = self.shipping_client.dict(found_collection)
            collections_dict_list.append(
                entities.Collection.from_dict(
                    self,
                    collection_dict
                )
            )
        return collections_dict_list

    @try_except
    def get_shipment(self, shipment_id):
        """
        Calls GetShipment from the Despatch Bay Shipping Service.
        """
        shipment_dict = self.shipping_client.dict(
            self.shipping_client.service.GetShipment(shipment_id))
        return entities.ShipmentReturn.from_dict(
            self,
            shipment_dict
        )

    @try_except
    def add_shipment(self, shipment_request):
        """
        Calls AddShipment from the Despatch Bay Shipping Service.
        """
        return self.shipping_client.service.AddShipment(shipment_request.to_soap_object())

    @try_except
    def book_shipments(self, shipment_ids):
        """
        Calls BookShipments from the Despatch Bay Shipping Service.
        """
        array_of_shipment_id = self.shipping_client.factory.create('ns1:ArrayOfShipmentID')
        array_of_shipment_id.item = shipment_ids
        booked_shipments_list = []
        for booked_shipment in self.shipping_client.service.BookShipments(array_of_shipment_id):
            booked_shipment_dict = self.shipping_client.dict(booked_shipment)
            booked_shipments_list.append(
                entities.ShipmentReturn.from_dict(
                    self,
                    booked_shipment_dict
                )
            )
        return booked_shipments_list

    @try_except
    def cancel_shipment(self, shipment_id):
        """
        Calls CancelShipment from the Despatch Bay Shipping Service.
        """
        return self.shipping_client.service.CancelShipment(shipment_id)

    # Tracking services

    @try_except
    def get_tracking(self, tracking_number):
        """
        Calls GetTracking from the Despatch Bay Tracking Service.
        """
        return self.tracking_client.service.GetTracking(tracking_number)

    # Documents services

    def fetch_shipment_labels(self, document_id, **kwargs):
        """
        Fetches labels from the Despatch Bay documents API.
        """
        return self.pdf_client.fetch_shipment_labels(document_id, **kwargs)

    def fetch_manifest(self, collection_id):
        """
        Fetches manifests from the Despatch Bay documents API.
        """
        return self.pdf_client.fetch_manifest(collection_id)
