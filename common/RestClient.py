import requests

from config import BASE_URL


class HttpClient:

    def __init__(self):
        self.session = requests.session()

    def send_request(self,method,url,**kwargs):

        pathurl = BASE_URL + url

        response = self.session.request(method=method.upper(), url=pathurl,**kwargs)
        return response



