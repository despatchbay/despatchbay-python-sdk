class Entity(object):

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
