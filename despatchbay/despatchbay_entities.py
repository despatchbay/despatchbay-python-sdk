"""
Entities relating to types in the Despatchbay v15 api
https://github.com/despatchbay/despatchbay-api-v15/wiki
"""


class Entity:
    """Base class for Despatchbay entities"""
    def __init__(self, soap_type, soap_client, soap_map):
        self.soap_type = soap_type
        self.soap_client = soap_client
        self.soap_map = soap_map

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.soap_client.factory.create(self.soap_type)
        for soap_property in self.soap_map:
            if self.soap_map[soap_property]['type'] == 'entity':
                setattr(
                    suds_object,
                    soap_property,
                    getattr(
                        self,
                        self.soap_map[soap_property]['property']).to_soap_object()
                )
            elif self.soap_map[soap_property]['type'] == 'entityArray':
                entity_list = []
                for entity in getattr(self, self.soap_map[soap_property]['property']):
                    entity_list.append(entity.to_soap_object())
                soap_array = self.soap_client.factory.create(self.soap_map[soap_property]['soap_type'])
                soap_array.item = entity_list
                soap_array._arrayType = 'urn:ArrayType[]'
                setattr(suds_object, soap_property, soap_array)
            else:
                setattr(
                    suds_object, soap_property, getattr(
                        self,
                        self.soap_map[soap_property]['property']
                    )
                )
        return suds_object

    def __repr__(self):
        return str(self.to_soap_object())


class Account(Entity):
    """
    Represents a Despactchbay API AccountType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Account-Service#accounttype
    """
    SOAP_MAP = {
        'AccountID': {
            'property': 'account_id',
            'type': 'integer'
        },
        'AccountName': {
            'property': 'name',
            'type': 'string'
        },
        'AccountBalance': {
            'property': 'balance',
            'type': 'entity',
            'soap_type': 'ns1:AccountBalanceType',
        }
    }
    SOAP_TYPE = 'ns1:AccountType'

    def __init__(self, client, account_id=None, name=None, balance=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.account_id = account_id
        self.name = name
        self.balance = balance

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            account_id=soap_dict.get('AccountID', None),
            name=soap_dict.get('AccountName', None),
            balance=AccountBalance.from_dict(
                client,
                client.account_client.dict(soap_dict.get('AccountBalance', None))
            )
        )


class AccountBalance(Entity):
    """
    Represents a Despactchbay API AccountBalanceType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Account-Service#accountbalancetype
    """
    SOAP_MAP = {
        'Balance': {
            'property': 'balance',
            'type': 'float'
        },
        'AvailableBalance': {
            'property': 'available',
            'type': 'float'
        }
    }
    SOAP_TYPE = 'ns1:AccountBalanceType'

    def __init__(self, client, balance=None, available=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.balance = balance
        self.available = available

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            balance=soap_dict.get('Balance', None),
            available=soap_dict.get('AvailableBalance', None)
        )


class Address(Entity):
    """
    Represents a Despactchbay API AddressType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Account-Service#addresstype
    """
    SOAP_MAP = {
        'CompanyName': {
            'property': 'company_name',
            'type': 'string',
        },
        'Street': {
            'property': 'street',
            'type': 'string',
        },
        'Locality': {
            'property': 'locality',
            'type': 'string',
        },
        'TownCity': {
            'property': 'town_city',
            'type': 'string',
        },
        'County': {
            'property': 'county',
            'type': 'string',
        },
        'PostalCode': {
            'property': 'postal_code',
            'type': 'string',
        },
        'CountryCode': {
            'property': 'country_code',
            'type': 'string',
        }
    }
    SOAP_TYPE = 'ns1:AddressType'

    def __init__(self, client, company_name=None, street=None, locality=None, town_city=None, county=None,
                 postal_code=None, country_code=None):
        super().__init__(self.SOAP_TYPE, client.addressing_client, self.SOAP_MAP)
        self.company_name = company_name
        self.street = street
        self.locality = locality
        self.town_city = town_city
        self.county = county
        self.postal_code = postal_code
        self.country_code = country_code

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative initialiser, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            company_name=soap_dict.get('CompanyName', None),
            street=soap_dict.get('Street', None),
            locality=soap_dict.get('Locality', None),
            town_city=soap_dict.get('TownCity', None),
            county=soap_dict.get('County', None),
            postal_code=soap_dict.get('PostalCode', None),
            country_code=soap_dict.get('CountryCode', None)
        )


class AddressKey(Entity):
    """
    Represents a Despactchbay API AddressKeyType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Addressing-Service#addresskeytype
    """
    SOAP_MAP = {
        'Key': {
            'property': 'key',
            'type': 'string',
        },
        'Address': {
            'property': 'address',
            'type': 'string',
        }
    }
    SOAP_TYPE = 'ns1:AddressKeyType'

    def __init__(self, client, key, address):
        super().__init__(self.SOAP_TYPE, client.addressing_client, self.SOAP_MAP)
        self.key = key
        self.address = address

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            key=soap_dict.get('Key', None),
            address=soap_dict.get('Address', None)
        )


class AutomaticTopupSettings(Entity):
    """
    Represents a Despactchbay API AutomaticTopupSettings entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Account-Service#automatictopupsettings
    """
    SOAP_MAP = {
        "MinimumBalance": {
            "property": "minimum_balance",
            "type": "float"
        },
        "TopupAmount": {
            "property": "topup_amount",
            "type": "float"
        },
        "PaymentMethodID": {
            "property": "payment_method_id",
            "type": "string"
        }
    }
    SOAP_TYPE = 'ns1:AutomaticTopupsSettingsRequestType'

    def __init__(self, client, minimum_balance=None, topup_amount=None, payment_method_id=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.minimum_balance = minimum_balance
        self.topup_amount = topup_amount
        self.payment_method_id = payment_method_id

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            minimum_balance=soap_dict.get('MinimumBalance', None),
            topup_amount=soap_dict.get('TopupAmount', None),
            payment_method_id=soap_dict.get('PaymentMethodID', None)
        )


class Collection(Entity):
    """
    Represents a Despactchbay API CollectionType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#collectionreturntype
    """
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
        self.despatchbay_client = client
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
            date=CollectionDate.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('CollectionDate'))
            ),
            sender_address=Sender.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('SenderAddress', None))
            ),
            collection_courier=Courier.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('Courier', None))
            ),
            labels_url=soap_dict.get('LabelsURL', None),
            manifest_url=soap_dict.get('Manifest', None)
        )

    def get_labels(self, **kwargs):
        """
        Fetches label pdf through the Despatch Bay API client.
        """
        return self.despatchbay_client.get_labels(self.document_id, **kwargs)

    def get_manifest(self, **kwargs):
        """
        Fetches menifest pdf through the Despatch Bay API client.
        """
        return self.despatchbay_client.get_manifest(self.document_id, **kwargs)


class CollectionDate(Entity):
    """
    Represents a Despactchbay API CollectionDateType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#collectiondatetype
    """
    SOAP_MAP = {
        "CollectionDate": {
            "property": "date",
            "type": "string"
        }
    }
    SOAP_TYPE = 'ns1:CollectionDateType'

    def __init__(self, client, date=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.date = date

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            date=soap_dict.get('CollectionDate', None)
        )


class Courier(Entity):
    """
    Represents a Despactchbay API CourierType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#couriertype
    """
    SOAP_MAP = {
        'CourierID': {
            'property': 'courier_id',
            'type': 'integer'
        },
        'CourierName': {
            'property': 'name',
            'type': 'string'
        }
    }
    SOAP_TYPE = 'ns1:CourierType'

    def __init__(self, client, courier_id=None, name=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.courier_id = courier_id
        self.name = name

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            courier_id=soap_dict.get('CourierID', None),
            name=soap_dict.get('CourierName', None)
        )


class Parcel(Entity):
    """
    Represents a Despactchbay API ParcelType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#parceltype
    """
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


class PaymentMethod(Entity):
    """
    Represents a Despactchbay API PaymentMethodType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Account-Service#paymentmethodtype
    """
    SOAP_MAP = {
        'PaymentMethodID': {
            'property': 'payment_method_id',
            'type': 'integer'
        },
        'Type': {
            'property': 'payment_method_type',
            'type': 'string'
        },
        'Description': {
            'property': 'description',
            'type': 'string'
        }
    }
    SOAP_TYPE = 'ns1:PaymentMethodType'

    def __init__(self, client, payment_method_id=None, payment_method_type=None, description=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.payment_method_id = payment_method_id
        self.payment_method_type = payment_method_type
        self.description = description

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            payment_method_id=soap_dict.get('PaymentMethodID', None),
            payment_method_type=soap_dict.get('Type', None),
            description=soap_dict.get('Description', None)
        )


class Recipient(Entity):
    """
    Represents a Despactchbay API RecipientAddressType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#recipientaddresstype
    """
    SOAP_MAP = {
        'RecipientName': {
            'property': 'name',
            'type': 'string',
        },
        'RecipientTelephone': {
            'property': 'telephone',
            'type': 'string',
        },
        'RecipientEmail': {
            'property': 'email',
            'type': 'string',
        },
        'RecipientAddress': {
            'property': 'recipient_address',
            'type': 'entity',
            'soap_type': 'ns1:RecipientAddressType',
        },
    }
    SOAP_TYPE = 'ns1:RecipientAddressType'

    def __init__(self, client, name=None, telephone=None, email=None, recipient_address=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.name = name
        self.telephone = telephone
        self.email = email
        self.recipient_address = recipient_address

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            name=soap_dict.get('RecipientName', None),
            telephone=soap_dict.get('RecipientTelephone', None),
            email=soap_dict.get('RecipientEmail', None),
            recipient_address=Address.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('RecipientAddress', None))
            )
        )


class Sender(Entity):
    """
    Represents a Despactchbay API SenderAddressType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#senderaddresstype
    """
    SOAP_MAP = {
        'SenderName': {
            'property': 'name',
            'type': 'string',
        },
        'SenderTelephone': {
            'property': 'telephone',
            'type': 'string',
        },
        'SenderEmail': {
            'property': 'email',
            'type': 'string',
        },
        'SenderAddress': {
            'property': 'sender_address',
            'type': 'entity',
            'soap_type': 'ns1:SenderAddress',

        },
        'SenderAddressID': {
            'property': 'address_id',
            'type': 'integer',
        },
    }
    SOAP_TYPE = 'ns1:SenderAddressType'

    def __init__(self, client, name=None, telephone=None, email=None, sender_address=None, address_id=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.name = name
        self.telephone = telephone
        self.email = email
        if sender_address:
            self.sender_address = sender_address
        else:
            self.sender_address = Address(client)
        self.address_id = address_id

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            name=soap_dict.get('SenderName', None),
            telephone=soap_dict.get('SenderTelephone', None),
            email=soap_dict.get('SenderEmail', None),
            sender_address=Address.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('SenderAddress', None))
            ),
            address_id=soap_dict.get('SenderAddressID')
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.

        Removes sender address property if a sender address id is provided.
        """
        soap_object = super().to_soap_object()
        if soap_object.SenderAddressID:
            soap_object.SenderAddress = None
        return soap_object


class Service(Entity):
    """
    Represents a Despactchbay API ServiceType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#servicetype
    """
    SOAP_MAP = {
        'ServiceID': {
            'property': 'service_id',
            'type': 'integer'
        },
        'Format': {
            'property': 'service_format',
            'type': 'string'
        },
        'Name': {
            'property': 'name',
            'type': 'string'
        },
        'Cost': {
            'property': 'cost',
            'type': 'currency',
        },
        'Courier': {
            'property': 'courier',
            'type': 'entity',
            'soap_type': 'ns1:CourierType',

        },
    }
    SOAP_TYPE = 'ns1:ServiceType'

    def __init__(self, client, service_id, service_format, name, cost, courier):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.service_id = service_id
        self.format = service_format
        self.name = name
        self.cost = cost
        self.courier = courier

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            service_id=soap_dict.get('ServiceID', None),
            service_format=soap_dict.get('Format', None),
            name=soap_dict.get('Name', None),
            cost=soap_dict.get('Cost', None),
            courier=Courier.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('Courier', None))
            )
        )


class ShipmentRequest(Entity):
    """
    Represents a Despactchbay API ShipmentRequest entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#shipmentrequesttype
    """
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
            'soap_type': 'ns1:CollectionDateType',
        },
        'RecipientAddress': {
            'property': 'recipient_address',
            'type': 'entity',
            'soap_type': 'ns1:RecipientAddressType',
        },
        'SenderAddress': {
            'property': 'sender_address',
            'type': 'entity',
            'soap_type': 'ns1:SenderAddressType',
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
        self.despatchbay_client = client
        self.service_id = service_id
        self.parcels = parcels
        self.client_reference = client_reference
        self._collection_date = self.validate_collection_date_object(collection_date)
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.follow_shipment = follow_shipment

    def validate_collection_date_object(self, collection_date):
        """
        Converts a string timestamp to a CollectionDate object.
        """
        if isinstance(collection_date, str):
            return CollectionDate(self.despatchbay_client, date=collection_date)
        return collection_date

    @property
    def collection_date(self):
        """
        Returns the private attribute collection_date
        """
        return self._collection_date

    @collection_date.setter
    def collection_date(self, collection_date):
        """
        Allows the collection date to be set from just a timestamp string but limits the
        type of the _collection_date attribute to a CollectionDate object.
        """
        self._collection_date = self.validate_collection_date_object(collection_date)


class ShipmentReturn(Entity):
    """
    Represents a Despactchbay API ShipmentReturnType entity.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Shipping-Service#shipmentreturntype
    """
    SOAP_MAP = {
        'ShipmentID': {
            'property': 'shipment_id',
            'type': 'string',
        },
        'ShipmentDocumentID': {
            'property': 'shipment_document_id',
            'type': 'string',
        },
        'CollectionID': {
            'property': 'collection_id',
            'type': 'string',
        },
        'CollectionDocumentID': {
            'property': 'collection_document_id',
            'type': 'string',
        },
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
        'RecipientAddress': {
            'property': 'recipient_address',
            'type': 'entity',
            'soap_type': 'ns1:RecipientAddressType',
        },
        'IsFollowed': {
            'property': 'is_followed',
            'type': 'boolean',
        },
        'IsPrinted': {
            'property': 'is_printed',
            'type': 'boolean',
        },
        'IsDespatched': {
            'property': 'is_despatched',
            'type': 'boolean',
        },
        'IsDelivered': {
            'property': 'is_delivered',
            'type': 'boolean',
        },
        'IsCancelled': {
            'property': 'is_cancelled',
            'type': 'boolean',
        },
        'LabelsURL': {
            'property': 'labels_url',
            'type': 'boolean',
        },
    }
    SOAP_TYPE = 'ns1:ShipmentReturnType'

    def __init__(self, client, shipment_id=None, shipment_document_id=None, collection_id=None,
                 collection_document_id=None, service_id=None, parcels=None, client_reference=None,
                 recipient_address=None, is_followed=None, is_printed=None, is_despatched=None,
                 is_delivered=None, is_cancelled=None, labels_url=None):
        super().__init__(self.SOAP_TYPE, client.shipping_client, self.SOAP_MAP)
        self.despatchbay_client = client
        self.shipment_id = shipment_id
        self.shipment_document_id = shipment_document_id
        self.collection_id = collection_id
        self.collection_document_id = collection_document_id
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
                Parcel.from_dict(
                    client,
                    client.shipping_client.dict(parcel_item)
                )
            )
        return cls(
            client=client,
            shipment_id=soap_dict.get('ShipmentID'),
            shipment_document_id=soap_dict.get('ShipmentDocumentID'),
            collection_id=soap_dict.get('CollectionID'),
            collection_document_id=soap_dict.get('CollectionDocumentID'),
            service_id=soap_dict.get('ServiceID'),
            parcels=parcel_array,
            client_reference=soap_dict.get('ClientReference'),
            recipient_address=Recipient.from_dict(
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

    def book(self):
        """
        Makes a BookShipment request through the Despatch Bay API client.
        """
        book_return = self.despatchbay_client.book_shipments([self.shipment_id])
        if book_return:
            self.shipment_document_id = book_return[0].shipment_document_id
            self.collection_id = book_return[0].collection_id
            self.collection_document_id = book_return[0].collection_document_id
            self.labels_url = book_return[0].labels_url
        return book_return[0]

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
        return self.despatchbay_client.get_labels(self.shipment_document_id, **kwargs)
