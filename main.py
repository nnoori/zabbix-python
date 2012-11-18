# -*- coding: utf-8 -*-
import logging

from zabbix.session import Session
from zabbix.application import Application
from zabbix.application import ApplicationSearch
from zabbix.hostgroup import Hostgroup
from zabbix.hostgroup import HostgroupSearch

logging.basicConfig(level=logging.DEBUG)
sesion = Session("http://192.168.1.12/zabbix", "admin", "zabbix", pretty_debug=True)

hgs = HostgroupSearch()
hgs.name = "My*"
hg = Hostgroup.get(hgs)

hg.name = "My Name2"

hg.save()

