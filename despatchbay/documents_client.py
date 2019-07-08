"""
Classes for working with the despatchbay documents api

https://github.com/despatchbay/despatchbay-api-v15/wiki/Documents-API
"""

from urllib.parse import urlencode
import base64

import requests

from . import exceptions


class Document:
    """
    A document (label/manifest) in the despatchbay documents api.

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Documents-API
    """
    def __init__(self, data):
        self.data = data

    def get_raw(self):
        """
        Returns the raw data used to create the entity.
        """
        return self.data

    def get_base64(self):
        """
        Base 64 encodes the document data before returning it.
        """
        return base64.b64encode(self.data)

    def download(self, path):
        """
        Saves the file to the specified location.
        """
        with open(path, 'wb') as document_file:
            document_file.write(self.data)


class DocumentsClient:
    """
    Client for the despatchbay documents api

    https://github.com/despatchbay/despatchbay-api-v15/wiki/Documents-API
    """
    def __init__(self, api_url='http://api.despatchbay.com/documents/v1'):
        self.api_url = api_url

    @staticmethod
    def handle_response_code(code, response):
        """
        Returns true if code is 200, otherwise raises an appropriate exception.
        """
        if code == 200:
            return True
        if code == 400:
            raise exceptions.InvalidArgumentException(
                'The Documents API was unable to process the request: {}'.format(response))
        if code == 401:
            raise exceptions.AuthorizationException('Unauthorized')
        if code == 402:
            raise exceptions.PaymentException('Insufficient Despatch Bay account balance')
        if code == 404:
            raise exceptions.ApiException('Unknown shipment ID')
        raise exceptions.ApiException('An unexpected error occurred (HTTP {})'.format(code))

    def fetch_shipment_labels(self, document_ids, label_layout=None, label_format=None, label_dpi=None):
        """
         Returns a document entity of the shipment labels identified by document_ids which can be a comma
         separated string of shipment IDs.
        """
        if isinstance(document_ids, list):
            shipment_string = ','.join(document_ids)
        else:
            shipment_string = document_ids
        query_dict = {}
        if label_layout:
            query_dict['layout'] = label_layout
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
        self.handle_response_code(response.status_code, response.text)
        return Document(response.content)

    def fetch_manifest(self, collection_document_id, manifest_format=None):
        """
         Returns a document entity of the shipment manifest identified by collection_id.
        """
        manifest_request_url = '{}/manifest/{}'.format(self.api_url, collection_document_id)
        if manifest_format:
            manifest_request_url = '{}?format={}'.format(manifest_request_url, manifest_format)
        response = requests.get(manifest_request_url)
        self.handle_response_code(response.status_code, response.text)
        return Document(response.content)
