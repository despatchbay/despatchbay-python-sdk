import base64


class Pdf(object):
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
        Saves the PDF to the specified location.
        """
        with open(path, 'wb') as pdf_file:
            pdf_file.write(self.data)

