# -*- coding: utf-8 -*-

import attr

from troposphere import (
    BaseAWSObject,
    AWSHelperFn,
)
from .sentiel import NOTHING


# Monkey Patch AWSHelperFn
def getdata(self, data):
    """
    .. note::

        由于 troposphere 中对于 Ref, Fn 接 AWSObject 的时候, 是取其 title, 而
        mate.AWSObject 并没有被该方法所检测到, 所以我们用 monkey patch 将其补上.
    """
    if isinstance(data, (BaseAWSObject, AWSObject)):
        return data.title
    else:
        return data


AWSHelperFn.getdata = getdata

non_properties_attrs = {
    "title", "template", "validation"
}


@attr.s
class AWSObject(object):
    title = None
    template = attr.ib(default=None)
    validation = attr.ib(default=True)

    _aws_object_class = None
    _aws_object = NOTHING  # type: BaseAWSObject

    def _convert_value(self, value):
        """
        
        :param value: 
        :return:
        
        .. note::
        
            由于 mate.AWSObject 的属性本身可能是另一个 mate.AWSObject, 又或者是一个
            list of mate.AWSObject. 所以我们要递归滴将其转化为 troposphere.AWSObject,
            然后传递给 troposphere.AWSObject.__init__ 函数.
        
            这里我们不能使用 attr.asdict 方法, 因为它会讲所有 nested 的 对象也转化为
            字典, 而不是 troposphere.AWSObject 实例.
        """
        if isinstance(value, AWSObject):
            return value.aws_object
        elif isinstance(value, (list, tuple, set)):
            new_value = list()
            for item in value:
                if isinstance(item, AWSObject):
                    new_value.append(item.aws_object)
                else:
                    new_value.append(item)
            return new_value
        else:
            return value

    def _convert_aws_object(self, title, template=None, validation=True):
        dct = dict()
        for key, value in attr.asdict(self, recurse=False).items():
            if value is not NOTHING:
                dct[key] = self._convert_value(value)
        dct["title"] = title
        dct["template"] = template
        dct["validation"] = validation
        return self._aws_object_class(**dct)

    @property
    def aws_object(self):
        """
        :rtype: TroposphereAWSObject
        :return:

        .. note::

            troposphere_mate 的基本原理是在 __init__ 之后, 将对应的
            troposphere.AWSObject 的实例保存在 ._aws_object 属性中, 且这是一个单例.

            虽然说 aws_object 是一个 property method, 但是无论执行多少次, 都返回的是
            一个单例. 这事为了避免 1 个 mate.AWSObject 跟多个 troposphere.AWSObject
            对应. 因为之后 mate.AWSObject 的 attribute 可能会发生改变 (为了跟
            troposphere.AWSObject 的 API 保持一致). 




        """
        if self._aws_object is NOTHING:
            self._aws_object = self._convert_aws_object(
                title=self.title,
                template=self.template,
                validation=self.validation,
            )
        return self._aws_object

    def update_aws_object(self):
        """

        :return:

        .. note::

            当 mate.AWSObject 的属性发生修改时, 变化不会自动反映到 mate.AWSObject._aws_object
            中. 由于 API 的限制, 我们不希望改动 attr 的 setattr API, 所以, 我选择
            使用 update_aws_object 方法, 手动将变化应用到 ._aws_object.

            由于生成 troposphere.AWSObject.__init__ 时, 有可能会将其自动与 Template 绑定,
            而我们要的仅仅是改变数据, 所以在这里我们显示地阻止其与 Template 绑定.
        """
        for key, value in attr.asdict(self, recurse=False).items():
            if (key not in non_properties_attrs) and (value is not NOTHING):
                setattr(self.aws_object, key, self._convert_value(value))

    def __attrs_post_init__(self):
        """

        :return:

        .. note::

            在 mate.AWSObject 调用 __init__ 时, 对应的 troposphere.AWSObject.__init__
            也要被执行.
        """
        _ = self.aws_object  # call self.aws_object once

    def add_to_template(self):
        return self.aws_object.add_to_template()

    def to_dict(self):
        return self.aws_object.to_dict()
