from urllib.parse import urlencode
from entities import pdf
import requests
import base64


class PdfClient(object):
    API_URI = 'http://api.despatchbay.st/documents/v1/labels'

    def __init__(self, credentials, user_agent):
        self.auth = {
            'apiuser': credentials['apiUser'],
            'apikey': credentials['apiKey']
        }
        self.user_agent = user_agent

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
        r = requests.get(label_request_url)
        if label_format == 'png_base64' or label_format == 'pdf_base64':
            label_data = base64.b64decode(r.content)
        else:
            label_data = r.content
        return pdf.Pdf(label_data)

    def fetch_manifest(self, collection_id):
        manifest_request_url = '{}/{}'.format(self.API_URI,
                                              collection_id)
        r = requests.get(manifest_request_url)
        return pdf.Pdf(r.content)

