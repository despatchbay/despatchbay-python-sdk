import base64

class Pdf(object):

    def __init__(self, data):
        # if self.is_pdf(data):
        self.data = data
        print(self.data)
        # else:
        #     pass
        #     # print(data)
        #     # raise TypeError("Apparently not a PDF")

    def is_pdf(self):
        return self.data[0:4] == '%PDF'

    def get_raw(self):
        return self.data

    def get_base64(self):
        return base64.b64decode(self.data)

    #todo how to send to browser

    def download(self, path):
        with open(path, 'wb') as pdf_file:
            pdf_file.write(self.data)

