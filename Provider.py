import requests
import urllib3
import json
import random

DEFAULT_TIMEOUT = 30
VERIFY = True
not VERIFY and urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning)

with open('config.json', 'r') as f:
    PROVIDERS = json.load(f)['providers']


class Provider:
    def __init__(self, target, proxy={}, verbose=False, cc='91', config=None):
        if config:
            self.config = config
        else:
            self.config = random.choice(PROVIDERS[cc] +
                                        PROVIDERS['multi'] if cc in
                                        PROVIDERS else PROVIDERS['multi'])
        self.target = target
        self.headers = self._headers()
        self.done = False
        self.proxy = proxy
        self.cookies = self._cookies()
        self.verbose = verbose
        self.cc = cc

    def _headers(self):
        tmp_headers = {
            "User-Agent":
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        }
        if 'headers' in self.config:
            tmp_headers.update(self.config['headers'])
        return tmp_headers

    def _cookies(self):
        tmp_cookies = {}
        if 'cookies' in self.config:
            tmp_cookies.update(self.config['cookies'])
        return tmp_cookies

    def _data(self):
        tmp_data = {}
        for key, value in self.config['data'].items():
            tmp_data[key] = value.format(cc=self.cc, target=self.target)
        return tmp_data

    def _params(self):
        tmp_params = {}
        if 'params' in self.config:
            for key, value in self.config['params'].items():
                tmp_params[key] = value.format(cc=self.cc, target=self.target)
        return tmp_params

    def _get(self):
        return requests.get(self.config['url'],
                            params=self.params,
                            headers=self.headers,
                            cookies=self.cookies,
                            timeout=DEFAULT_TIMEOUT,
                            proxies=self.proxy,
                            verify=VERIFY)

    def _post(self):
        return requests.post(self.config['url'],
                             data=self.data,
                             headers=self.headers,
                             cookies=self.cookies,
                             timeout=10,
                             proxies=self.proxy,
                             verify=VERIFY)

    def start(self):
        if self.config['method'] == 'GET':
            self.params = self._params()
            self.resp = self._get()
        elif self.config['method'] == 'POST':
            self.data = self._data()
            self.resp = self._post()
        self.done = True

    def status(self):
        if self.config['identifier'] in self.resp.text:
            self.verbose and print('{:12}: success'.format(
                self.config['name']))
            return True
        else:
            self.verbose and print('{:12}: failed'.format(self.config['name']))
            return False
