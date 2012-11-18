# -*- coding: utf-8 -*-
from zabbix.base import SearchBase
from zabbix.base import ReadableObject
from zabbix.base import WriteableObject
from zabbix.base import DeleteableObject

from zabbix.host import Host

from zabbix.internal.parameters import BooleanParameter
from zabbix.internal.parameters import StringParameter
from zabbix.internal.parameters import ObjectParameter
from zabbix.internal.parameters import IndentifiersParameter


class Application(ReadableObject, WriteableObject, DeleteableObject):

    _id_param = StringParameter("applicationid")
    _host_param = ObjectParameter("hostid", Host)
    _name_param = StringParameter("name")
    _template_param = ObjectParameter("templateid", Host)

    def __init__(self):
        super(Application, self).__init__()

    @classmethod
    def get_prefix(self):
        return "application"

    identifier = property(_id_param.get, None, None, "Identifier")
    host = property(_host_param.get, _host_param.set, None, "Host")
    name = property(_name_param.get, _name_param.set, None, "Name")
    template = property(_template_param.get, None, None, "Template (Read Only)")


class ApplicationSearch(SearchBase):

    _applications_param = IndentifiersParameter("applicationids", Application)
    _groups_param = IndentifiersParameter("groupids", Application)
    _hosts_param = IndentifiersParameter("hostids", Application)
    _inherited_param = BooleanParameter("inherited", False)
    _item_param = IndentifiersParameter("itemids", Application)
    _templated_param = BooleanParameter("templated", False)

    def __init__(self):
        super(ApplicationSearch, self).__init__()
        self._zabbix_format["expandData"] = True

    applications = property(_applications_param.get, _applications_param.set, None, "Name parameter")
    groups = property(_groups_param.get, _groups_param.set, None, "Name parameter")
    inherited = property(_inherited_param.get, _inherited_param.set, None, "Name parameter")
    hosts = property(_hosts_param.get, _hosts_param.set, None, "Name parameter")
