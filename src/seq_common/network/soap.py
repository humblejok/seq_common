'''
Created on Oct 22, 2013

FROM: http://stackoverflow.com/questions/6277027/suds-over-https-with-cert

@author: sdejonckheere
'''
import requests
from suds.transport.http import HttpAuthenticated
from suds.transport import Reply

class RequestsTransport(HttpAuthenticated):
    def __init__(self, **kwargs):
        self.cert = kwargs.pop('cert', None)
        # super won't work because not using new style class
        HttpAuthenticated.__init__(self, **kwargs)

    def send(self, request):
        self.addcredentials(request)
        resp = requests.post(request.url, data=request.message,
                             headers=request.headers, verify=False, cert=self.cert)
        result = Reply(resp.status_code, resp.headers, resp.content)
        return result