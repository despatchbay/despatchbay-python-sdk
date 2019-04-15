import base64

class Pdf(object):

    def __init__(self, data):
        if self.is_pdf(data):
            self.data = data
        else:
            raise TypeError("File returned from api is not a valid PDF.")

    @staticmethod
    def is_pdf(data):
        return data[0:4].decode() == '%PDF'

    def get_raw(self):
        return self.data

    def get_base64(self):
        return base64.b64decode(self.data)

    def download(self, path):
        with open(path, 'wb') as pdf_file:
            pdf_file.write(self.data)

