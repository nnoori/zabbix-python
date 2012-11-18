# -*- coding: utf-8 -*-
from zabbix.base import SearchBase
from zabbix.base import ReadableObject
from zabbix.base import WriteableObject
from zabbix.base import DeleteableObject

from zabbix.host import Host

from zabbix.internal.parameters import BooleanParameter
from zabbix.internal.parameters import StringParameter
#from zabbix.internal.parameters import ObjectParameter
#from zabbix.internal.parameters import IndentifiersParameter


class Hostgroup(ReadableObject, WriteableObject, DeleteableObject):

    _id_param = StringParameter("groupid")
    _name_param = StringParameter("name")
    _internal_param = BooleanParameter("internal", Host)

    def __init__(self):
        super(Hostgroup, self).__init__()

    @classmethod
    def get_prefix(self):
        return "hostgroup"

    identifier = property(_id_param.get, None, None, "Identifier")
    name = property(_name_param.get, _name_param.set, None, "Name")
    internal = property(_internal_param.get, None, None, "Internal (Read Only)")


class HostgroupSearch(SearchBase):

    _name_param = StringParameter("name")
    #_applications_param = IndentifiersParameter("applicationids", Application)
    #_groups_param = IndentifiersParameter("groupids", Application)
    #_hosts_param = IndentifiersParameter("hostids", Application)
    #_inherited_param = BooleanParameter("inherited", False)
    #_item_param = IndentifiersParameter("itemids", Application)
    #_templated_param = BooleanParameter("templated", False)

    def __init__(self):
        super(HostgroupSearch, self).__init__()
#        self._zabbix_format["expandData"] = True

    name = property(_name_param.get, _name_param.set, None, "Name")
    #applications = property(_applications_param.get, _applications_param.set, None, "Name parameter")
    #groups = property(_groups_param.get, _groups_param.set, None, "Name parameter")
    #inherited = property(_inherited_param.get, _inherited_param.set, None, "Name parameter")
    #hosts = property(_hosts_param.get, _hosts_param.set, None, "Name parameter")
#