from entity import Entity


class Address(Entity):
    def __init__(self, client, company_name, street, locality, town_city, county, postal_code, country_code):

        Entity.__init__(self, client)

        self.type_name = 'ns1:AddressType'
        self.suds_object = self.client.factory.create(self.type_name)

        self.suds_object.CompanyName = company_name
        self.suds_object.Street = street
        self.suds_object.Locality = locality
        self.suds_object.TownCity = town_city
        self.suds_object.County = county
        self.suds_object.PostalCode = postal_code
        self.suds_object.CountryCode = country_code

    def get_soap_object(self):
        return self.suds_object
