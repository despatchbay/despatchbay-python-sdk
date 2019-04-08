class Address(object):
    def __init__(self, client, company_name, street, locality, town_city, county, postal_code, country_code):
        self.client = client
        self.type_name = 'ns1:AddressType'
        self.company_name = company_name
        self.street = street
        self.locality = locality
        self.town_city = town_city
        self.county = county
        self.postal_code = postal_code
        self.country_code = country_code

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.CompanyName = self.company_name
        suds_object.Street = self.street
        suds_object.Locality = self.locality
        suds_object.TownCity = self.town_city
        suds_object.County = self.county
        suds_object.PostalCode = self.postal_code
        suds_object.CountryCode = self.country_code
        return suds_object
