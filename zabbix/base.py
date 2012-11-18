# -*- coding: utf-8 -*-
from zabbix.session import Session
from zabbix.exceptions import NoneUniqueResultException


class _BaseObject(object):

    _zabbix_format = None

    @classmethod
    def _call(cls, method, data):
        return Session._get_instance().call(method, data)

    @classmethod
    def _get_parameters(cls):
        return cls._allowed_parameters

    @classmethod
    def _get_prefix(cls):
        return cls._prefix

    def __init__(self):
        self._zabbix_format = dict()
        pass

    def __str__(self):
        return repr(self._zabbix_format)

    def __repr__(self):
        return repr(self._zabbix_format)

    def _build(self, json_string):
        self._zabbix_format = json_string

    def __setattr__(self, name, value):
        if (name in dir(self)):
            super(_BaseObject, self).__setattr__(name, value)
            return
        else:
            raise Exception("%s is not an alllowed parameter" % name)


class ReadableObject(_BaseObject):

    def __init__(self):
        super(ReadableObject, self).__init__()

    @classmethod
    def get(cls, search_criteria):
        search_criteria._zabbix_format["output"] = "extend"
        call_result = cls._call("%s.get" % cls.get_prefix(), search_criteria._zabbix_format)

        if len(call_result) == 0:
            return None

        if len(call_result) > 1:
            raise NoneUniqueResultException("Found more than one result")

        result = cls()
        result._build(call_result[0])

        return result

    @classmethod
    def find(cls, search_criteria):
        search_criteria._zabbix_format["output"] = "extend"
        call_results = cls._call("%s.get" % cls.get_prefix(), search_criteria._zabbix_format)

        results = []
        for call_result in call_results:
            result = cls()
            result._build(call_result)
            results.append(result)
        return results

    @classmethod
    def count(cls, search_criteria):
        search_criteria._internal["countOutput"] = True
        return int(cls._call("%s.get" % cls.get_prefix(), search_criteria._zabbix_format))


class WriteableObject(_BaseObject):

    def __init__(self):
        super(WriteableObject, self).__init__()

    def save(self):
        if self.identifier:
            self._call("%s.update" % self.get_prefix(), self._zabbix_format)
        else:
            self._call("%s.create" % self.get_prefix(), self._zabbix_format)


class DeleteableObject(_BaseObject):

    def __init__(self):
        super(DeleteableObject, self).__init__()

    def delete(self):
        pass


class SearchBase(_BaseObject):

    def __init__(self):
        super(SearchBase, self).__init__()
