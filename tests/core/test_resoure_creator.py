# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

import sys
import pytest

from troposphere_mate.core.code import flatten_dct


def jprint(dct):
    print(json.dumps(dct, indent=4, sort_keys=False))


def jprint_items(items):
    jprint(OrderedDict(
        sorted(
            items,
            key=lambda x: x[0]
        )
    ))


def test_flatten_dct():
    dct = {
        "id": "pid0001",
        "passport": {
            "id": "pass2020",
            "info": {
                "issued_country": "USA",
                "issued_date": "2000-01-01",
            },
            "history": [
                {
                    "issued_country": "France",
                    "issued_date": "1990-01-01",
                },
                {
                    "issued_country": "England",
                    "issued_date": "1995-01-01",
                },
            ]
        },
        "tags": [
            {"key": "first_name", "value": "Alice"},
            {"key": "last_name", "value": "Smith"},
        ],
        "character": ["nice", "friendly"],
    }
    # jprint(flatten_dct(dct))
    if sys.version_info.major == 2:
        return

    assert flatten_dct(dct) == [
        [
            "id",
            "pid0001"
        ],
        [
            "passport.id",
            "pass2020"
        ],
        [
            "passport.info.issued_country",
            "USA"
        ],
        [
            "passport.info.issued_date",
            "2000-01-01"
        ],
        [
            "passport.history.[0].issued_country",
            "France"
        ],
        [
            "passport.history.[0].issued_date",
            "1990-01-01"
        ],
        [
            "passport.history.[1].issued_country",
            "England"
        ],
        [
            "passport.history.[1].issued_date",
            "1995-01-01"
        ],
        [
            "tags.[0].key",
            "first_name"
        ],
        [
            "tags.[0].value",
            "Alice"
        ],
        [
            "tags.[1].key",
            "last_name"
        ],
        [
            "tags.[1].value",
            "Smith"
        ],
        [
            "character.[0]",
            "nice"
        ],
        [
            "character.[1]",
            "friendly"
        ]
    ]
    # jprint_items(flatten_dct(dct))


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
