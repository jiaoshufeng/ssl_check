#!/usr/bin/env python3
from urllib3.contrib import pyopenssl
from datetime import datetime
from sys import argv


class SSL_Check:
    
    def __init__(self, url):
        self.url = url
    
    @property
    def get_str_time(self):
        x509 = pyopenssl.OpenSSL.crypto.load_certificate(pyopenssl.OpenSSL.crypto.FILETYPE_PEM,
                                                    pyopenssl.ssl.get_server_certificate((self.url, 443)))
        return x509.get_notAfter().decode()[0:-1]
    @property
    def get_ssl_time(self):
        ssl_time = datetime.strptime(self.get_str_time,'%Y%m%d%H%M%S')
        return (ssl_time - datetime.now()).days


if __name__ == '__main__':
    try:
        url = argv[1]
        ssl_chenk=SSL_Check(url)
        print(ssl_chenk.get_ssl_time)
    except Exception as e:
        print('')