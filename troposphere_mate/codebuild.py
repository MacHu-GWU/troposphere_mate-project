# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.codebuild

from troposphere.codebuild import Artifacts
from troposphere.codebuild import CloudWatchLogs
from troposphere.codebuild import Environment
from troposphere.codebuild import GitSubmodulesConfig
from troposphere.codebuild import LogsConfig
from troposphere.codebuild import ProjectCache
from troposphere.codebuild import ProjectTriggers
from troposphere.codebuild import RegistryCredential
from troposphere.codebuild import S3Logs
from troposphere.codebuild import Source
from troposphere.codebuild import SourceAuth
from troposphere.codebuild import Tags
from troposphere.codebuild import VpcConfig
from troposphere.codebuild import boolean
from troposphere.codebuild import integer
from troposphere.codebuild import positive_integer
from troposphere.codebuild import validate_credentials_provider
from troposphere.codebuild import validate_image_pull_credentials
from troposphere.codebuild import validate_status
from troposphere.codebuild import validate_webhookfilter_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class SourceAuth(AWSObject):
    
    Type = attr.ib() # type: str
    Resource = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.SourceAuth


@attr.s
class Artifacts(AWSObject):
    
    Type = attr.ib() # type: str
    ArtifactIdentifier = attr.ib(default=NOTHING) # type: str
    EncryptionDisabled = attr.ib(default=NOTHING) # type: boolean
    Location = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    NamespaceType = attr.ib(default=NOTHING) # type: str
    OverrideArtifactName = attr.ib(default=NOTHING) # type: boolean
    Packaging = attr.ib(default=NOTHING) # type: str
    Path = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.Artifacts


@attr.s
class EnvironmentVariable(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str
    Type = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.EnvironmentVariable


@attr.s
class RegistryCredential(AWSObject):
    
    Credential = attr.ib() # type: str
    CredentialProvider = attr.ib() # type: validate_credentials_provider

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.RegistryCredential


@attr.s
class Environment(AWSObject):
    
    ComputeType = attr.ib() # type: str
    Image = attr.ib() # type: str
    Type = attr.ib() # type: str
    Certificate = attr.ib(default=NOTHING) # type: str
    EnvironmentVariables = attr.ib(default=NOTHING) # type: tuple
    ImagePullCredentialsType = attr.ib(default=NOTHING) # type: validate_image_pull_credentials
    PrivilegedMode = attr.ib(default=NOTHING) # type: boolean
    RegistryCredential = attr.ib(default=NOTHING) # type: RegistryCredential

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.Environment


@attr.s
class ProjectCache(AWSObject):
    
    Type = attr.ib() # type: str
    Location = attr.ib(default=NOTHING) # type: str
    Modes = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.ProjectCache


@attr.s
class GitSubmodulesConfig(AWSObject):
    
    FetchSubmodules = attr.ib() # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.GitSubmodulesConfig


@attr.s
class Source(AWSObject):
    
    Type = attr.ib() # type: str
    Auth = attr.ib(default=NOTHING) # type: SourceAuth
    BuildSpec = attr.ib(default=NOTHING) # type: str
    GitCloneDepth = attr.ib(default=NOTHING) # type: positive_integer
    GitSubmodulesConfig = attr.ib(default=NOTHING) # type: GitSubmodulesConfig
    InsecureSsl = attr.ib(default=NOTHING) # type: boolean
    Location = attr.ib(default=NOTHING) # type: str
    ReportBuildStatus = attr.ib(default=NOTHING) # type: boolean
    SourceIdentifier = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.Source


@attr.s
class VpcConfig(AWSObject):
    
    SecurityGroupIds = attr.ib() # type: list
    Subnets = attr.ib() # type: list
    VpcId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.VpcConfig


@attr.s
class WebhookFilter(AWSObject):
    
    Pattern = attr.ib() # type: str
    Type = attr.ib() # type: validate_webhookfilter_type
    ExcludeMatchedPattern = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.WebhookFilter


@attr.s
class ProjectTriggers(AWSObject):
    
    Webhook = attr.ib(default=NOTHING) # type: boolean
    FilterGroups = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.ProjectTriggers


@attr.s
class CloudWatchLogs(AWSObject):
    
    Status = attr.ib() # type: validate_status
    GroupName = attr.ib(default=NOTHING) # type: str
    StreamName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.CloudWatchLogs


@attr.s
class S3Logs(AWSObject):
    
    Status = attr.ib() # type: validate_status
    EncryptionDisabled = attr.ib(default=NOTHING) # type: boolean
    Location = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.S3Logs


@attr.s
class LogsConfig(AWSObject):
    
    CloudWatchLogs = attr.ib(default=NOTHING) # type: CloudWatchLogs
    S3Logs = attr.ib(default=NOTHING) # type: S3Logs

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.LogsConfig


@attr.s
class ProjectSourceVersion(AWSObject):
    
    SourceIdentifier = attr.ib() # type: str
    SourceVersion = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.ProjectSourceVersion


@attr.s
class Project(AWSObject):
    title = attr.ib()   # type: str
    
    Artifacts = attr.ib() # type: Artifacts
    Environment = attr.ib() # type: Environment
    ServiceRole = attr.ib() # type: str
    Source = attr.ib() # type: Source
    BadgeEnabled = attr.ib(default=NOTHING) # type: boolean
    Cache = attr.ib(default=NOTHING) # type: ProjectCache
    Description = attr.ib(default=NOTHING) # type: str
    EncryptionKey = attr.ib(default=NOTHING) # type: str
    LogsConfig = attr.ib(default=NOTHING) # type: LogsConfig
    Name = attr.ib(default=NOTHING) # type: str
    SecondaryArtifacts = attr.ib(default=NOTHING) # type: list
    SecondarySourceVersions = attr.ib(default=NOTHING) # type: list
    SecondarySources = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags
    TimeoutInMinutes = attr.ib(default=NOTHING) # type: integer
    Triggers = attr.ib(default=NOTHING) # type: ProjectTriggers
    VpcConfig = attr.ib(default=NOTHING) # type: VpcConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codebuild.Project
