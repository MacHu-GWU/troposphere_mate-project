# -*- coding: utf-8 -*-

from troposphere_mate import Template, Tags, Ref, Output
from troposphere_mate import Select, GetAZs
from troposphere_mate import awslambda, apigateway
from troposphere_mate.core.canned import MultiEnvBasicConfig, Constant, Derivable


class Config(MultiEnvBasicConfig):
    method = {}

    class RestApiMethods:
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        PATCH = "PATCH"
        DELET = "DELETE"
        ANY = "ANY"
