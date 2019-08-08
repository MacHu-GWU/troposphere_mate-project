# -*- coding: utf-8 -*-

from troposphere_mate.core.canned import MultiEnvBasicConfig


class Config(MultiEnvBasicConfig):
    method = {}

    class RestApiMethods:
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        PATCH = "PATCH"
        DELET = "DELETE"
        ANY = "ANY"
        HEAD = "HEAD"
        OPTION = "OPTION"
