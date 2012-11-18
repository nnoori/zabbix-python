# -*- coding: utf-8 -*-
import logging
from zabbix.internal.transport import Transport


class Session(object):

    @staticmethod
    def _get_instance():
        return Session._instance

    def __init__(self, server_url, username, password, **kwargs):
        self.username = username
        self.password = password
        self.log = logging.getLogger('zabbix')
        self.transport = Transport(server_url, username, password, **kwargs)

        Session._instance = self

    def call(self, method, parameters):
        return self.transport.call_zabbix(method, parameters)