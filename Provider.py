import requests
import json
import random


class Provider:

    def __init__(self, target, proxy={}, verbose=False, cc='91'):
        try:
            self.config = random.choice(
                json.load(open('config.json', 'r'))['providers'][cc])
        except:
            self.config = random.choice(
                json.load(open('config.json', 'r'))['providers']['multi'])
        self.target = target
        self.headers = self._headers()
        self.done = False
        self.proxy = proxy
        self.verbose = verbose
        self.cc = cc

    def _headers(self):
        tmp_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"}
        if 'headers' in self.config:
            for key, value in self.config['headers'].items():
                tmp_headers[key] = value
        if 'data_type' in self.config and self.config['data_type'].lower() == "json":
            tmp_headers['Content-Type'] = 'application/json'
            self.data_type = 'json'
        else:
            tmp_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            self.data_type = 'urlencoded'
        return tmp_headers

    def _data(self):
        data = self.config['data']
        if 'cc_target' in self.config:
            data[self.config['cc_target']] += self.cc
        data[self.config['target_param']] += self.target
        return data

    def _get(self):
        url = self.config['url'] + self.target
        if 'cc_target' in self.config:
            url += '&' + self.config['cc_target'] + '=' + self.cc
        return requests.get(url, headers=self.headers, timeout=10, proxies=self.proxy)

    def _post(self):
        if self.data_type == "json":
            return requests.post(self.config['url'], json=self.data, headers=self.headers, timeout=10, proxies=self.proxy)
        elif self.data_type == "urlencoded":
            return requests.post(self.config['url'], data=self.data, headers=self.headers, timeout=10, proxies=self.proxy)

    def start(self):
        if self.config['method'] == 'GET':
            self.resp = self._get()
        elif self.config['method'] == 'POST':
            self.data = self._data()
            self.resp = self._post()
        self.done = True

    def status(self):
        if self.config['identifier'] in self.resp.text:
            self.verbose and print(
                '{:12}: success'.format(self.config['name']))
            return True
        else:
            self.verbose and print('{:12}: failed'.format(self.config['name']))
            return False
