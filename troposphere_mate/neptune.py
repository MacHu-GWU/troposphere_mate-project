# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.neptune

from troposphere.neptune import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DBClusterParameterGroup(troposphere.neptune.DBClusterParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 Family=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=REQUIRED, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Family=Family,
            Parameters=Parameters,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(DBClusterParameterGroup, self).__init__(**processed_kwargs)


class DBCluster(troposphere.neptune.DBCluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AvailabilityZones=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 BackupRetentionPeriod=NOTHING, # type: int
                 DBClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBClusterParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DBSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 IamAuthEnabled=NOTHING, # type: bool
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 PreferredBackupWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageEncrypted=NOTHING, # type: bool
                 Tags=NOTHING, # type: _Tags
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AvailabilityZones=AvailabilityZones,
            BackupRetentionPeriod=BackupRetentionPeriod,
            DBClusterIdentifier=DBClusterIdentifier,
            DBClusterParameterGroupName=DBClusterParameterGroupName,
            DBSubnetGroupName=DBSubnetGroupName,
            IamAuthEnabled=IamAuthEnabled,
            KmsKeyId=KmsKeyId,
            Port=Port,
            PreferredBackupWindow=PreferredBackupWindow,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            SnapshotIdentifier=SnapshotIdentifier,
            StorageEncrypted=StorageEncrypted,
            Tags=Tags,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(DBCluster, self).__init__(**processed_kwargs)


class DBInstance(troposphere.neptune.DBInstance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBInstanceClass=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowMajorVersionUpgrade=NOTHING, # type: bool
                 AutoMinorVersionUpgrade=NOTHING, # type: bool
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 DBClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBInstanceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DBSnapshotIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBInstanceClass=DBInstanceClass,
            AllowMajorVersionUpgrade=AllowMajorVersionUpgrade,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            AvailabilityZone=AvailabilityZone,
            DBClusterIdentifier=DBClusterIdentifier,
            DBInstanceIdentifier=DBInstanceIdentifier,
            DBParameterGroupName=DBParameterGroupName,
            DBSnapshotIdentifier=DBSnapshotIdentifier,
            DBSubnetGroupName=DBSubnetGroupName,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            Tags=Tags,
            **kwargs
        )
        super(DBInstance, self).__init__(**processed_kwargs)


class DBParameterGroup(troposphere.neptune.DBParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 Family=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=REQUIRED, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Family=Family,
            Parameters=Parameters,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(DBParameterGroup, self).__init__(**processed_kwargs)


class DBSubnetGroup(troposphere.neptune.DBSubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBSubnetGroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 DBSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBSubnetGroupDescription=DBSubnetGroupDescription,
            SubnetIds=SubnetIds,
            DBSubnetGroupName=DBSubnetGroupName,
            Tags=Tags,
            **kwargs
        )
        super(DBSubnetGroup, self).__init__(**processed_kwargs)
