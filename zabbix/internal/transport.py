# -*- coding: utf-8 -*-
import logging
import json
import urllib2
import pprint

from zabbix.exceptions import TransportException
from zabbix.exceptions import AlreadyExistsException


class Transport(object):

    request_headers = {
        'Content-Type': 'application/json-rpc',
        'User-Agent': 'python/zabbix_api'}

    def __init__(self, server_url, username, password, **kwargs):
        self.server = server_url
        self.username = username
        self.password = password
        self.log = logging.getLogger('zabbix').getChild('transport')
        self.requestid = 0
        self.auth = ''
        self.url = server_url + '/api_jsonrpc.php'

        self.timeout = kwargs.get("timeout", 10)
        self.pretty_print_debug = kwargs.get("pretty_debug", False)

    def _debug(self, sending, json_obj):

        if not self.log.isEnabledFor(logging.DEBUG):
            return

        json_output = json.dumps(json_obj)
        if self.pretty_print_debug:
            json_output = pprint.pformat(json_obj, indent=2, width=20)

        message = "Received: %s"
        if sending:
            message = "Sending: %s"

        self.log.debug(message, json_output)

    def _build_request(self, method, parameters):
        obj = {'jsonrpc': '2.0',
               'method': method,
               'params': parameters,
               'auth': self.auth,
               'id': self.requestid}

        return obj

    def _send_request(self, request_data):
        self._debug(True, request_data)

        request_string = json.dumps(request_data)
        request = urllib2.Request(url=self.url, data=request_string, headers=Transport.request_headers)
        http_handler = urllib2.HTTPHandler()
        opener = urllib2.build_opener(http_handler)
        urllib2.install_opener(opener)
        response = opener.open(request, timeout=self.timeout)
        reads = response.read()

        return reads

    def _parse_response(self, response):
        if len(response) == 0:
            raise Exception("Received zero answer")
        try:
            response_obj = json.loads(response.decode('utf-8'))
        except ValueError:
            raise TransportException("unable to decode. returned string: %s" % response)

        self._debug(False, response_obj)

        error_obj = response_obj.get("error")
        if error_obj:
            if int(error_obj.get("code")) == -32602 and "already exists" in error_obj.get("data"):
                raise AlreadyExistsException(error_obj["data"])
            else:
                raise TransportException(error_obj)

        return response_obj['result']

    def _login(self):
        request = self._build_request("user.authenticate", {"user": self.username, "password": self.password})
        response = self._send_request(request)
        self.auth = self._parse_response(response)
        self.log.info("Set auth to : " + self.auth)
        self.requestid += 1

    def call_zabbix(self, method, parameters):
        self.requestid += 1
        if self.auth == "":
            self._login()

        request = self._build_request(method, parameters)
        response = self._send_request(request)
        return self._parse_response(response)
