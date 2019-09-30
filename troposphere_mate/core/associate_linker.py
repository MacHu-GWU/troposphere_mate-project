# -*- coding: utf-8 -*-

"""
This module provides auto AWSResource Association Linker.
"""

try:
    import typing
except: # pragma: no cover
    pass

import inspect
from six import add_metaclass
from collections import OrderedDict, deque
from troposphere import AWSObject, depends_on_helper

SEP = " with "


def create_resource_type_key(resource_type_list):
    """
    :type resource_type_list: typing.List[typing.Type[typing.Any]]
    """
    resource_type_name_list = list()
    for resource_type in resource_type_list:
        try:
            resource_type_name_list.append(resource_type.resource_type)
        except:
            pass
    resource_type_name_list.sort()
    return SEP.join(resource_type_name_list)


DEPENDS_ON = "DependsOn"


def x_depends_on_y(x, y):
    """
    Define that x depends on y.

    :type x: AWSObject
    :type y: AWSObject
    """
    if not isinstance(y, AWSObject):
        raise TypeError("y can't be a string in x_depends_on_y(x, y)!")

    y_logic_id = depends_on_helper(y)

    if DEPENDS_ON not in x.resource:
        x.resource[DEPENDS_ON] = [y_logic_id, ]
    elif x.resource[DEPENDS_ON] is None:
        x.resource[DEPENDS_ON] = [y_logic_id, ]
    elif isinstance(x.resource[DEPENDS_ON], list):
        if y_logic_id not in x.resource[DEPENDS_ON]:
            x.resource[DEPENDS_ON].append(y_logic_id)
    else:
        if y_logic_id != x.resource[DEPENDS_ON]:
            x.resource[DEPENDS_ON] = [x.resource[DEPENDS_ON], y_logic_id]


class Linker(object):
    rtype1 = None  # type: AWSObject
    rtype2 = None  # type: AWSObject
    rtype3 = None  # type: AWSObject
    rtype4 = None  # type: AWSObject
    rtype5 = None  # type: AWSObject
    rtype6 = None  # type: AWSObject
    rtype7 = None  # type: AWSObject
    rtype8 = None  # type: AWSObject
    rtype9 = None  # type: AWSObject
    rtype10 = None  # type: AWSObject

    _creation_index = 0
    _identifier = None # type: str
    _rtype_ordered_list = None # type: typing.List[str]

    def __init__(self):
        rtype_ordered_list = list()
        resource_type_list = list()
        for rtype_key in _linker_rtype_keys:
            rtype = getattr(self, rtype_key)
            if rtype is not None:
                rtype_ordered_list.append(rtype.resource_type)
                resource_type_list.append(rtype)

        self.rtype_ordered_list = rtype_ordered_list
        self.identifier = create_resource_type_key(resource_type_list)

        self._creation_index = Linker._creation_index  # type: int
        Linker._creation_index += 1

    def associate(self, *args, **kwargs):
        raise NotImplementedError


_linker_rtype_keys = [
    k
    for k in Linker.__dict__ if k.startswith("rtype")
]


def is_instance_or_subclass(val, class_):
    """Return True if ``val`` is either a subclass or instance of ``class_``."""
    try:
        return issubclass(val, class_)
    except TypeError:
        return isinstance(val, class_)


def _get_fields(attrs, field_class, pop=False, ordered=False):
    """Get fields from a class. If ordered=True, fields will sorted by creation index.
    :param attrs: Mapping of class attributes
    :param type field_class: Base field class
    :param bool pop: Remove matching fields
    """
    fields = []
    for field_name, field_value in attrs.items():
        if is_instance_or_subclass(field_value, field_class):
            try:
                if issubclass(field_value, field_class):
                    linker = field_value()
            except TypeError:
                linker = field_value
            fields.append((linker.identifier, linker))

            field_value._identifier = linker.identifier
            field_value._rtype_ordered_list = linker.rtype_ordered_list

    if pop:  # pragma: no cover
        for field_name, _ in fields:
            del attrs[field_name]
    if ordered:
        fields.sort(key=lambda pair: pair[1]._creation_index)
    return fields


def _get_fields_by_mro(klass, field_class, ordered=False):
    """Collect fields from a class, following its method resolution order. The
    class itself is excluded from the search; only its parents are checked. Get
    fields from ``_declared_fields`` if available, else use ``__dict__``.
    :param type klass: Class whose fields to retrieve
    :param type field_class: Base field class
    """
    mro = inspect.getmro(klass)
    # Loop over mro in reverse to maintain correct order of fields
    return sum(
        (
            _get_fields(
                getattr(base, "_declared_linkers", base.__dict__),
                field_class,
                ordered=ordered,
            )
            for base in mro[:0:-1]
        ),
        [],
    )


class LinkerApiMeta(type):
    def __new__(cls, name, bases, attrs):
        """
        **中文文档**

        将所有在类属性中定义的 Linker Class 的类都搜集起来, 并且为这些类生成 identifier
        和 rtype_ordered_list, 以供高阶 LinkerApi.associate 函数将参数推送到相应的
        Linker.associate 方法中去.
        """
        cls_linkers = _get_fields(attrs, Linker, pop=False, ordered=True)
        klass = super(LinkerApiMeta, cls).__new__(cls, name, bases, attrs)
        inherited_linkers = _get_fields_by_mro(klass, Linker, ordered=True)

        # Assign _declared_fields on class
        klass._declared_linkers = OrderedDict(inherited_linkers + cls_linkers)
        return klass


class BaseLinkerApi(object):
    """
    """
    _declared_linkers = dict()

    @classmethod
    def associate(cls, *args, **kwargs):
        """
        :type args: typing.List[typing.BaseAWSObject]

        **中文文档**

        将杂乱顺序的输入参数, 按照 Linker 中 rtype1 - 10 的定义顺序, 重新排列,
        并传给 Linker.associate 函数执行.
        """
        identifier = create_resource_type_key(args)
        if identifier in cls._declared_linkers:
            linker_class = cls._declared_linkers[identifier]  # type: Linker
        else:
            msg = ("Association for {} has't not supported yet in troposphere_mate! "
                   "Please submit your sugggestion to "
                   "https://github.com/MacHu-GWU/troposphere_mate-project/issues").format(identifier)
            raise NotImplementedError(msg)

        resource_object_list = list()

        tmp_mapper = dict()
        for aws_object in args:
            try:
                tmp_mapper[aws_object.resource_type].append(aws_object)
            except:
                tmp_mapper[aws_object.resource_type] = deque([aws_object, ])

        for resource_type in linker_class.rtype_ordered_list:
            resource_object_list.append(tmp_mapper[resource_type].popleft())

        return linker_class.associate(*resource_object_list, **kwargs)


@add_metaclass(LinkerApiMeta)
class _LinkerApi(BaseLinkerApi):
    pass


class BaseAWSResource(object):
    resource_type = None

    def __init__(self, name):
        self.name = name


class DummyAWSResource1(BaseAWSResource):
    resource_type = "Res1"


class DummyAWSResource2(BaseAWSResource):
    resource_type = "Res2"


class DummyAWSResource3(BaseAWSResource):
    resource_type = "Res3"


class LinkerApi(_LinkerApi):
    # Test Linker
    class AWSResource1WithAWSResource2WithAWSResource3Tester(Linker):
        rtype1 = DummyAWSResource3
        rtype2 = DummyAWSResource2
        rtype3 = DummyAWSResource2
        rtype4 = DummyAWSResource1

        def associate(self, res1, res2_1, res2_2, res3, **kwargs):
            return [
                res1.name,
                res2_1.name,
                res2_2.name,
                res3.name,
            ]
