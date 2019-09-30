# -*- coding: utf-8 -*-

from . import (
    lbd_func,
    lbd_func_event_map,
    lbd_permission,
    apigw,
    ec2,
)


class LinkerApi(
    lbd_func.LinkerApi,
    lbd_func_event_map.LinkerApi,
    lbd_permission.LinkerApi,
    apigw.LinkerApi,
    ec2.LinkerApi,
): pass


def associate(*args, **kwargs):
    LinkerApi.associate(*args, **kwargs)
