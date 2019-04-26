from urllib.parse import urlencode
from . import exceptions
import requests
import base64

class Document(object):
    def __init__(self, data):
        if self.is_pdf(data):
            self.data = data
        else:
            raise TypeError("File returned from api is not a valid PDF.")

    @staticmethod
    def is_pdf(data):
        """
        Performs a rudimentary check to see if the data APPEARS to be a
        valid POF file.
        """
        return data[0:4].decode() == '%PDF'

    def get_raw(self):
        """
        Returns the raw data used to create the entity.
        """
        return self.data

    def get_base64(self):
        """
        Base 64 encodes the PDF data before returning it.
        """
        return base64.b64decode(self.data)

    def download(self, path):
        """
        Saves the file to the specified location.
        """
        with open(path, 'wb') as document_file:
            document_file.write(self.data)


class DocumentsClient(object):
    def __init__(self, api_url='http://api.despatchbay.com/documents/v1'):
        self.api_url = api_url

    @staticmethod
    def handle_response_code(code):
        """
        Returns true if code is 200, otherwise raises an appropriate exception.
        """
        if code == 200:
            return True
        elif code == 400:
            raise exceptions.InvalidArgumentException('The PDF Labels API was unable to process the request')
        elif code == 401:
            raise exceptions.AuthorizationException('Unauthorized')
        elif code == 402:
            raise exceptions.PaymentException('Insufficient Despatch Bay account balance')
        elif code == 404:
            raise exceptions.ApiException('Unknown shipment ID')
        else:
            raise exceptions.ApiException('An unexpected error occurred (HTTP {})'.format(code))

    def fetch_shipment_labels(self, ship_collect_ids, layout=None, label_format=None, label_dpi=None):
        """
         Returns a pdf entity of the shipment labels identified by ship_collect_ids.
        """
        if isinstance(ship_collect_ids, list):
            shipment_string = ','.join(ship_collect_ids)
        else:
            shipment_string = ship_collect_ids
        query_dict = {}
        if layout:
            query_dict['layout'] = layout
        if label_format:
            query_dict['format'] = label_format
            if label_format == 'png_base64' and label_dpi:
                query_dict['dpi'] = label_dpi
        label_request_url = '{}/labels/{}'.format(self.api_url,
                                                  shipment_string)
        if query_dict:
            query_string = urlencode(query_dict)
            label_request_url = label_request_url + '?' + query_string
        response = requests.get(label_request_url)
        self.handle_response_code(response.status_code)
        return Document(response.content)

    def fetch_manifest(self, collection_id):
        """
         Returns a pdf entity of the shipment manifest identified by collection_id.
        """
        manifest_request_url = '{}/manifest/{}'.format(self.api_url, collection_id)
        response = requests.get(manifest_request_url)
        self.handle_response_code(response.status_code)
        return Document(response.content)
