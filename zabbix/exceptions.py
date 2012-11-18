# -*- coding: utf-8 -*-


class ZabbixException(Exception):
    pass


class TransportException(ZabbixException):
    pass


class AlreadyExistsException(ZabbixException):
    pass


class NoneUniqueResultException(ZabbixException):
    pass