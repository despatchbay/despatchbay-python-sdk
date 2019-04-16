from urllib.parse import urlencode
from entities import pdf
import requests
import base64

import exception


class PdfClient(object):
    API_URI = 'http://api.despatchbay.st/documents/v1/labels'

    def __init__(self, credentials, ):
        self.auth = {
            'api_user': credentials['api_user'],
            'api_key': credentials['api_key']
        }

    def handle_response_code(self, code):
        if code == 200:
            return True
        elif code == 400:
            raise exception.InvalidArgumentException('The PDF Labels API was unable to process the request')
        elif code == 401:
            raise exception.AuthorizationException('Unauthorized')
        elif code == 402:
            raise exception.PaymentException('Insufficient Despatch Bay account balance')
        elif code == 404:
            raise exception.ApiException('Unknown shipment ID')
        else:
            raise exception.ApiException('An unexpected error occurred (HTTP {})'.format(code))

    def fetch_shipment_labels(self, ship_collect_ids, layout=None, label_format=None,
                              label_dpi=None):
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
        label_request_url = '{}/{}'.format(self.API_URI,
                                           shipment_string)
        if query_dict:
            query_string = urlencode(query_dict)
            label_request_url = label_request_url + '?' + query_string
        print(label_request_url)
        response = requests.get(label_request_url)
        self.handle_response_code(response.status_code)
        if label_format == 'png_base64' or label_format == 'pdf_base64':
            label_data = base64.b64decode(response.content)
        else:
            label_data = response.content
        return pdf.Pdf(label_data)

    def fetch_manifest(self, collection_id):
        manifest_request_url = '{}/{}'.format(self.API_URI,
                                              collection_id)
        response = requests.get(manifest_request_url)
        self.handle_response_code(response.status_code)
        return pdf.Pdf(response.content)

