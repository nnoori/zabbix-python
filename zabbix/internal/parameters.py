# -*- coding: utf-8 -*-


class Parameter(object):

    def __init__(self, internal_name, default_value):
        self._internal_name = internal_name
        self._default_value = default_value

    def get(self, container):
        return container._zabbix_format.get(self._internal_name, self._default_value)

    def set(self, container, value):
        container._zabbix_format[self._internal_name] = value


class StringParameter(Parameter):

    def __init__(self, internal_name, default_value=None):
        super(StringParameter, self).__init__(internal_name, default_value=default_value)


class TimestampParameter(Parameter):

    def __init__(self, internal_name, default_value=None):
        super(TimestampParameter, self).__init__(internal_name, default_value=default_value)


class BooleanParameter(Parameter):

    def __init__(self, internal_name, default_value=False):
        super(BooleanParameter, self).__init__(internal_name, default_value=default_value)

    def get(self, container):
        value = super(BooleanParameter, self).get(container)
        if isinstance(value, bool):
            return value
        elif isinstance(value, str):
            return value.lower() in ('yes', 'true')


class EnumParameter(Parameter):

    def __init__(self, internal_name, legal_values, default_value=False):
        super(EnumParameter, self).__init__(internal_name, default_value=default_value)
        self._legal_values = legal_values

    def set(self, container, value):
        if value in self._legal_values:
            container._zabbix_format[self._internal_name] = value
        else:
            raise Exception("This value '%s' for %s.%s is not legal" % (value, container.get_prefix(), self._internal_name))


class ObjectParameter(Parameter):

    def __init__(self, internal_name, object_type, default_value=None):
        super(ObjectParameter, self).__init__(internal_name, default_value=default_value)
        self.object_type = object_type


class IndentifiersParameter(Parameter):

    def __init__(self, internal_name, object_type, default_value=[]):
        super(IndentifiersParameter, self).__init__(internal_name, default_value=default_value)
        self.object_type = object_type

    def _evaluate_single_value(self, value):
        if isinstance(value, self.object_type):
            return value.identifier

        if isinstance(value, str):
            return value

        if isinstance(value, bool):
            raise Exception("value is not an idenfier or zabbix object %s is of type %s" % (value, type(value)))

        if isinstance(value, int):
            return str(value)

        raise Exception("value is not an idenfier or zabbix object %s is of type %s" % (value, type(value)))

    def set(self, container, value):
        result = []
        if isinstance(value, list):
            for value_item in value:
                result.append(self._evaluate_single_value(value_item))
        else:
            result.append(self._evaluate_single_value(value))

        container._zabbix_format[self._internal_name] = result


class ListParameter(Parameter):

    def __init__(self, internal_name):
        super(ListParameter, self).__init__(internal_name, [])
