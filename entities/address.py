class Address(object):
    def __init__(self, client, company_name, street, locality, town_city, county, postal_code, country_code):
        self.addressing_client = client.addressing_client
        self.type_name = 'ns1:AddressType'
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
        Alternative constructor, builds entity object from a dictionary representation of
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

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.addressing_client.factory.create(self.type_name)
        suds_object.CompanyName = self.company_name
        suds_object.Street = self.street
        suds_object.Locality = self.locality
        suds_object.TownCity = self.town_city
        suds_object.County = self.county
        suds_object.PostalCode = self.postal_code
        suds_object.CountryCode = self.country_code
        return suds_object
