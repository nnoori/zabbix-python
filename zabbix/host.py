# -*- coding: utf-8 -*-
from zabbix.base import SearchBase
from zabbix.base import ReadableObject
from zabbix.base import WriteableObject
from zabbix.base import DeleteableObject

#from zabbix.maintenance import Maintenance

from zabbix.internal.parameters import StringParameter
from zabbix.internal.parameters import ListParameter
from zabbix.internal.parameters import EnumParameter
from zabbix.internal.parameters import TimestampParameter
from zabbix.internal.parameters import BooleanParameter
from zabbix.internal.parameters import ObjectParameter


class Host(ReadableObject, WriteableObject, DeleteableObject):

    _id_param = StringParameter("applicationid")
    _name_param = StringParameter("host")
    _available_param = EnumParameter("available", [0, 1, 2], 0)
    _disable_until_param = TimestampParameter("disable_until")
    _error_param = StringParameter("disable_until")
    _errors_from_param = TimestampParameter("errors_from")
    _ipmi_auth_param = EnumParameter("ipmi_authtype", [-1, 0, 1, 2, 4, 5, 6], -1)
    _ipmi_available_param = EnumParameter("ipmi_available", [0, 1, 2], 0)
    _impi_disable_until_param = TimestampParameter("ipmi_disable_until")
    _ipmi_error_param = StringParameter("ipmi_error")
    _ipmi_errors_from_param = TimestampParameter("ipmi_errors_from")
    _ipmi_password_param = StringParameter("ipmi_password")
    _ipmi_privilege_param = EnumParameter("ipmi_privilege", [1, 2, 3, 4, 5], 1)
    _ipmi_username_param = StringParameter("ipmi_username")
    _jmx_available_param = EnumParameter("jmx_available", [0, 1, 2], 0)
    _jmx_disable_until_param = TimestampParameter("jmx_disable_until")
    _jmx_error_param = StringParameter("jmx_error")
    _jmx_errors_from_param = TimestampParameter("jmx_errors_from")
    _maintenance_from_param = TimestampParameter("maintenance_from")
    _maintenance_status_param = BooleanParameter("maintenance_from")
    _maintenance_type_param = EnumParameter("jmx_available", [0, 1], 0)
    #_maintenance_param = ObjectParameter("maintenanceid", Maintenance)
    _displayname_param = StringParameter("name")
    _proxy_param = ObjectParameter("proxy_hostid", None)
    _snmp_available_param = EnumParameter("snmp_available", [0, 1, 2], 0)
    _snmp_disable_until_param = TimestampParameter("snmp_disable_until")
    _snmp_error_param = StringParameter("snmp_error")
    _snmp_errors_from_param = TimestampParameter("snmp_errors_from")
    _status_param = EnumParameter("status", [0, 1], 0)

    @classmethod
    def get_prefix(self):
        return "host"

    def __init__(self):
        super(Host, self).__init__()
        self._proxy_param.object_type = Host

    AVAILABLE_UNKNOWN = 0
    AVAILABLE_TRUE = 1
    AVAILABLE_FALSE = 2

    IPMI_AUTH_DEFAULT = -1
    IPMI_AUTH_NONE = 0
    IPMI_AUTH_MD2 = 1
    IPMI_AUTH_MD5 = 2
    IPMI_AUTH_STRAIGHT = 4
    IPMI_AUTH_OEM = 5
    IPMI_AUTH_RMCP = 6

    IPMI_PRIVILEGE_CALLBACK = 1
    IPMI_PRIVILEGE_USER = 2
    IPMI_PRIVILEGE_OPERATOR = 3
    IPMI_PRIVILEGE_ADMIN = 4
    IPMI_PRIVILEGE_OEM = 5

    STATUS_MONITORED = 0
    STATUS_UNMONITORED = 1

    identifier = property(_id_param.get, _id_param.set, None, "Name parameter")
    available = property(_available_param.get, _available_param.set, None, "Name parameter")
    name = property(_name_param.get, _name_param.set, None, "")
    displayname = property(_displayname_param.get, _displayname_param.set, None, "")
    disable_until = property(_disable_until_param.get, None, None, "")
    error = property(_error_param.get, None, None, "")
    errors_from = property(_errors_from_param.get, None, None, "")
    proxy = property(_proxy_param.get, _proxy_param.set, None, "")
    status = property(_status_param.get, _status_param.set, None, "")

    ipmi_auth = property(_ipmi_auth_param.get, _ipmi_auth_param.set, None, "")
    ipmi_available = property(_ipmi_available_param.get, None, None, "")
    impi_disable_until = property(_impi_disable_until_param.get, None, None, "")
    ipmi_error = property(_ipmi_error_param.get, None, None, "")
    ipmi_errors_from = property(_ipmi_errors_from_param.get, None, None, "")
    ipmi_password = property(_ipmi_password_param.get, _ipmi_password_param.set, None, "")
    ipmi_privilege = property(_ipmi_privilege_param.get, _ipmi_privilege_param.set, None, "")
    ipmi_username = property(_ipmi_username_param.get, _ipmi_username_param.set, None, "")

    jmx_available = property(_jmx_available_param.get, None, None, "")
    jmx_disable_until = property(_jmx_disable_until_param.get, None, None, "")
    jmx_error = property(_jmx_error_param.get, None, None, "")
    jmx_errors_from = property(_jmx_errors_from_param.get, None, None, "")

    maintenance_from = property(_maintenance_from_param.get, None, None, "")
    maintenance_status = property(_maintenance_status_param.get, None, None, "")
    maintenance_type = property(_maintenance_type_param.get, None, None, "")
    #maintenance = property(_maintenance_param.get, None, None, "")

    snmp_available = property(_snmp_available_param.get, None, None, "")
    snmp_disable_until = property(_snmp_disable_until_param.get, None, None, "")
    snmp_error = property(_snmp_error_param.get, None, None, "")
    snmp_errors_from = property(_snmp_errors_from_param.get, None, None, "")


class HostSearch(SearchBase):

    _hosts_param = ListParameter("name")

    def __init__(self):
        super(HostSearch, self).__init__()

    hosts = property(_hosts_param.get, _hosts_param.set, None, "Name parameter")
