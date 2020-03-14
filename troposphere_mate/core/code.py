# -*- coding: utf-8 -*-

try:
    import typing
except:
    pass
import json
from collections import OrderedDict
from troposphere import kinesisanalyticsv2, glue, AWSObject, AWSProperty


def get_schema(resource):
    # if _schema is None:
    _schema = OrderedDict()
    for prop_name, (prop_type, required) in resource.props.items():
        try:
            issubclass(prop_type, AWSProperty)
            _schema[prop_name] = get_schema(prop_type)
        except:
            if isinstance(prop_type, list):
                try:
                    issubclass(prop_type[0], AWSProperty)
                    _schema[prop_name] = get_schema(prop_type[0])
                except:
                    _schema[prop_name] = None
            else:
                _schema[prop_name] = None
    return _schema


glue_table_json = """
{
    "Table": {
        "Name": "sign_up_counts",
        "DatabaseName": "test",
        "CreateTime": 1581648637.0,
        "UpdateTime": 1581648637.0,
        "Retention": 0,
        "StorageDescriptor": {
            "Columns": [
                {
                    "Name": "event_time",
                    "Type": "timestamp"
                },
                {
                    "Name": "sign_up_event_counts",
                    "Type": "smallint"
                }
            ],
            "Location": "s3://eq-sanhe-for-everything/data/kinesis-analytics/login-gov-metrics-dev",
            "Compressed": false,
            "NumberOfBuckets": 0,
            "SerdeInfo": {
                "SerializationLibrary": "org.openx.data.jsonserde.JsonSerDe",
                "Parameters": {
                    "serialization.format": "1"
                }
            },
            "SortColumns": [],
            "StoredAsSubDirectories": false
        },
        "PartitionKeys": [
            {
                "Name": "year",
                "Type": "smallint"
            },
            {
                "Name": "month",
                "Type": "smallint"
            },
            {
                "Name": "day",
                "Type": "smallint"
            },
            {
                "Name": "hour",
                "Type": "smallint"
            },
            {
                "Name": "minute",
                "Type": "smallint"
            }
        ],
        "TableType": "EXTERNAL_TABLE",
        "CreatedBy": "arn:aws:iam::110330507156:user/sanhe",
        "IsRegisteredWithLakeFormation": false
    }
}
""".strip()

def jprint(dct):
    print(json.dumps(dct, indent=4, sort_keys=True))



SEP = "."

def flatten_dct(dct, _items=None, _parent=None):
    """
    Convert a dict with nested dict or list into flattened key, value pairs.
    Key is in form of json path.

    :type dct: dict
    :rtype: typing.List[typing.Tuple[str, typing.Any]]
    """
    if _items is None:
        _items = list()
    if _parent is None:
        _parent = ""
    for key, value in dct.items():
        key = _parent + key
        if isinstance(value, dict):
            _items.extend(flatten_dct(value, _parent=key+SEP))
        elif isinstance(value, list):
            for ind, item in enumerate(value):
                _items.extend(flatten_dct({"[{}]".format(ind): item}, _parent=key+SEP))
        else:
            _items.append([key, value])
    return _items


def convert_data(dct, resource_type):
    schema = get_schema(resource_type)
    schema_flattened = flatten_dct(schema)
    jprint(schema_flattened)



if __name__ == "__main__":


    # schema = get_schema(kinesisanalyticsv2.Application)
    schema = get_schema(glue.Table)
    # schema = get_schema(kinesisanalyticsv2.Input)
    jprint(schema)
    # dct = json.loads(glue_table_json)
    # convert_data(dct, glue.Table)





    # print(json.dumps(schema, indent=4))