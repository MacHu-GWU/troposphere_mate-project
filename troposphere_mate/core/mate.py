# -*- coding: utf-8 -*-

from .sentiel import NOTHING, REQUIRED


def preprocess_init_kwargs(**kwargs):
    processed_kwargs = dict()
    for key, value in kwargs.items():
        if value is not NOTHING:
            processed_kwargs[key] = value
    return processed_kwargs
