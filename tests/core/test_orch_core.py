# -*- coding: utf-8 -*-

import pytest
from troposphere_mate.core.orch_core import resolve_pipeline, extract_all_env_tag


def test_extract_all_env_tag():
    assert extract_all_env_tag([
        ["T1", "dev"],
        ["T1", "test"],
        ["T1", "prod"],
        ["T2", "dev"],
        ["T3", "dev"],
        ["T2", "test"],
        ["T3", "test"],
        ["T2", "prod"],
        ["T3", "prod"],
    ]) == ["dev", "test", "prod"]


def test_resolve_pipeline():
    expected = [
        (['T1'], 'dev'),
        (['T1'], 'test'),
        (['T1'], 'prod'),
        (['T1', 'T2', 'T3'], 'dev'),
        (['T1', 'T2', 'T3'], 'test'),
        (['T1', 'T2', 'T3'], 'prod'),
    ]
    assert resolve_pipeline([
        ["T1", "dev"],
        ["T1", "test"],
        ["T1", "prod"],
        ["T2", "dev"],
        ["T3", "dev"],
        ["T2", "test"],
        ["T3", "test"],
        ["T2", "prod"],
        ["T3", "prod"],
    ]) == expected

    expected = [
        (['T1', 'T2'], 'dev'),
        (['T1', 'T2'], 'test'),
        (['T1', 'T2'], 'prod'),
        (['T1', 'T2', 'T3'], 'dev'),
        (['T1', 'T2', 'T3'], 'test'),
        (['T1', 'T2', 'T3'], 'prod'),
    ]
    assert resolve_pipeline([
        ["T1", "dev"],
        ["T2", "dev"],
        ["T1", "test"],
        ["T2", "test"],
        ["T1", "prod"],
        ["T2", "prod"],
        ["T3", "dev"],
        ["T3", "test"],
        ["T3", "prod"],
    ]) == expected

    expected = [
        (['T1', 'T2', 'T3'], 'dev'),
        (['T1', ], 'test'),
        (['T1', ], 'prod'),
        (['T1', 'T2'], 'test'),
        (['T1', 'T2'], 'prod'),
        (['T1', 'T2', 'T3'], 'test'),
        (['T1', 'T2', 'T3'], 'prod'),
    ]
    assert resolve_pipeline([
        ["T1", "dev"],
        ["T2", "dev"],
        ["T3", "dev"],
        ["T1", "test"],
        ["T1", "prod"],
        ["T2", "test"],
        ["T2", "prod"],
        ["T3", "test"],
        ["T3", "prod"],
    ]) == expected

    expected = [
        (['T1', 'T2', 'T3'], 'dev'),
        (['T1', 'T2'], 'test'),
        (['T1', 'T2'], 'prod'),
        (['T1', 'T2', 'T3'], 'test'),
        (['T1', 'T2', 'T3'], 'prod'),
    ]
    assert resolve_pipeline([
        ["T1", "dev"],
        ["T2", "dev"],
        ["T3", "dev"],
        ["T1", "test"],
        ["T2", "test"],
        ["T1", "prod"],
        ["T2", "prod"],
        ["T3", "test"],
        ["T3", "prod"],
    ]) == expected

    # with deploy now signal
    expected = [
        (['T1', 'T2'], 'dev'),
        (['T1', 'T2', 'T3'], 'dev'),
        (['T1', ], 'test'),
        (['T1', 'T2', 'T3'], 'test'),
        (['T1', 'T2', 'T3'], 'prod'),
    ]
    result = resolve_pipeline([
        ["T1", "dev"],
        ["T2", "dev"],
        ["deploy", "now"],
        ["T3", "dev"],
        ["T1", "test"],
        ["deploy", "now"],
        ["T2", "test"],
        ["T3", "test"],
        ["T1", "prod"],
        ["T2", "prod"],
        ["T3", "prod"],
        ["deploy", "now"],
    ])
    assert result == expected

    expected = [
        (['T1', ], 'dev'),
        (['T1', 'T2'], 'dev'),
        (['T1', 'T2', 'T3'], 'dev'),
    ]
    result = resolve_pipeline([
        ["T1", "dev"],
        ["deploy", "now"],
        ["deploy", "now"],
        ["T2", "dev"],
        ["deploy", "now"],
        ["deploy", "now"],
        ["T3", "dev"],
    ])
    assert result == expected

    expected = [
        (['T1', 'T2'], 'dev'),
        (['T1', ], 'test'),
        (['T1', 'T2'], 'test'),
    ]
    result = resolve_pipeline([
        ["T1", "dev"],
        ["T2", "dev"],
        ["deploy", "now"],
        ["T1", "test"],
        ["deploy", "now"],
        ["T2", "test"],
    ])
    assert result == expected


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
