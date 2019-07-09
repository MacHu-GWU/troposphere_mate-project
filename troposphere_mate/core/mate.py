# -*- coding: utf-8 -*-

from .sentiel import NOTHING, REQUIRED
from .tagger import (
    tag_property_name_mapper,
    update_tags_for_resource,
    update_tags_for_template,
)
import troposphere

def preprocess_init_kwargs(**kwargs):
    processed_kwargs = dict()
    for key, value in kwargs.items():
        if value is not NOTHING:
            processed_kwargs[key] = value
    return processed_kwargs


class Mixin(object):
    @classmethod
    def get_tags_attr(cls):
        return tag_property_name_mapper.get(cls.resource_type)

    def update_tags(self, tags_dct, overwrite=False):
        update_tags_for_resource(self, tags_dct, overwrite=overwrite)


class Template(troposphere.Template):
    def update_tags(self, tags_dct, overwrite=False):
        update_tags_for_template(self, tags_dct, overwrite=overwrite)

    def pprint(self):
        print(self.to_json(indent=4))
