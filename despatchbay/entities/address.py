from entity import Entity


class Address(Entity):

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

