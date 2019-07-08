# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.cloudfront

from troposphere.cloudfront import CloudFrontOriginAccessIdentityConfig
from troposphere.cloudfront import Cookies
from troposphere.cloudfront import CustomOriginConfig
from troposphere.cloudfront import DefaultCacheBehavior
from troposphere.cloudfront import DistributionConfig
from troposphere.cloudfront import ForwardedValues
from troposphere.cloudfront import GeoRestriction
from troposphere.cloudfront import Logging
from troposphere.cloudfront import Restrictions
from troposphere.cloudfront import S3Origin
from troposphere.cloudfront import S3OriginConfig
from troposphere.cloudfront import StreamingDistributionConfig
from troposphere.cloudfront import TrustedSigners
from troposphere.cloudfront import ViewerCertificate
from troposphere.cloudfront import boolean
from troposphere.cloudfront import cloudfront_event_type
from troposphere.cloudfront import cloudfront_forward_type
from troposphere.cloudfront import cloudfront_restriction_type
from troposphere.cloudfront import cloudfront_viewer_protocol_policy
from troposphere.cloudfront import integer
from troposphere.cloudfront import network_port
from troposphere.cloudfront import positive_integer
from troposphere.cloudfront import priceclass_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Cookies(AWSObject):
    
    Forward = attr.ib() # type: cloudfront_forward_type
    WhitelistedNames = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.Cookies


@attr.s
class ForwardedValues(AWSObject):
    
    QueryString = attr.ib() # type: boolean
    Cookies = attr.ib(default=NOTHING) # type: Cookies
    Headers = attr.ib(default=NOTHING) # type: list
    QueryStringCacheKeys = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.ForwardedValues


@attr.s
class LambdaFunctionAssociation(AWSObject):
    
    EventType = attr.ib(default=NOTHING) # type: cloudfront_event_type
    LambdaFunctionARN = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.LambdaFunctionAssociation


@attr.s
class CacheBehavior(AWSObject):
    
    ForwardedValues = attr.ib() # type: ForwardedValues
    PathPattern = attr.ib() # type: str
    TargetOriginId = attr.ib() # type: str
    ViewerProtocolPolicy = attr.ib() # type: cloudfront_viewer_protocol_policy
    AllowedMethods = attr.ib(default=NOTHING) # type: list
    CachedMethods = attr.ib(default=NOTHING) # type: list
    Compress = attr.ib(default=NOTHING) # type: boolean
    DefaultTTL = attr.ib(default=NOTHING) # type: integer
    FieldLevelEncryptionId = attr.ib(default=NOTHING) # type: str
    LambdaFunctionAssociations = attr.ib(default=NOTHING) # type: list
    MaxTTL = attr.ib(default=NOTHING) # type: integer
    MinTTL = attr.ib(default=NOTHING) # type: integer
    SmoothStreaming = attr.ib(default=NOTHING) # type: boolean
    TrustedSigners = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.CacheBehavior


@attr.s
class DefaultCacheBehavior(AWSObject):
    
    ForwardedValues = attr.ib() # type: ForwardedValues
    TargetOriginId = attr.ib() # type: str
    ViewerProtocolPolicy = attr.ib() # type: cloudfront_viewer_protocol_policy
    AllowedMethods = attr.ib(default=NOTHING) # type: list
    CachedMethods = attr.ib(default=NOTHING) # type: list
    Compress = attr.ib(default=NOTHING) # type: boolean
    DefaultTTL = attr.ib(default=NOTHING) # type: integer
    FieldLevelEncryptionId = attr.ib(default=NOTHING) # type: str
    LambdaFunctionAssociations = attr.ib(default=NOTHING) # type: list
    MaxTTL = attr.ib(default=NOTHING) # type: integer
    MinTTL = attr.ib(default=NOTHING) # type: integer
    SmoothStreaming = attr.ib(default=NOTHING) # type: boolean
    TrustedSigners = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.DefaultCacheBehavior


@attr.s
class S3Origin(AWSObject):
    
    DomainName = attr.ib() # type: str
    OriginAccessIdentity = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.S3Origin


@attr.s
class CustomOriginConfig(AWSObject):
    
    OriginProtocolPolicy = attr.ib() # type: str
    HTTPPort = attr.ib(default=NOTHING) # type: network_port
    HTTPSPort = attr.ib(default=NOTHING) # type: network_port
    OriginKeepaliveTimeout = attr.ib(default=NOTHING) # type: integer
    OriginReadTimeout = attr.ib(default=NOTHING) # type: integer
    OriginSSLProtocols = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.CustomOriginConfig


@attr.s
class OriginCustomHeader(AWSObject):
    
    HeaderName = attr.ib() # type: str
    HeaderValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.OriginCustomHeader


@attr.s
class S3OriginConfig(AWSObject):
    
    OriginAccessIdentity = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.S3OriginConfig


@attr.s
class Origin(AWSObject):
    
    DomainName = attr.ib() # type: str
    Id = attr.ib() # type: str
    CustomOriginConfig = attr.ib(default=NOTHING) # type: CustomOriginConfig
    OriginCustomHeaders = attr.ib(default=NOTHING) # type: list
    OriginPath = attr.ib(default=NOTHING) # type: str
    S3OriginConfig = attr.ib(default=NOTHING) # type: S3OriginConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.Origin


@attr.s
class Logging(AWSObject):
    
    Bucket = attr.ib() # type: str
    IncludeCookies = attr.ib(default=NOTHING) # type: boolean
    Prefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.Logging


@attr.s
class CustomErrorResponse(AWSObject):
    
    ErrorCode = attr.ib() # type: positive_integer
    ErrorCachingMinTTL = attr.ib(default=NOTHING) # type: positive_integer
    ResponseCode = attr.ib(default=NOTHING) # type: positive_integer
    ResponsePagePath = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.CustomErrorResponse


@attr.s
class GeoRestriction(AWSObject):
    
    RestrictionType = attr.ib() # type: cloudfront_restriction_type
    Locations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.GeoRestriction


@attr.s
class Restrictions(AWSObject):
    
    GeoRestriction = attr.ib() # type: GeoRestriction

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.Restrictions


@attr.s
class ViewerCertificate(AWSObject):
    
    AcmCertificateArn = attr.ib(default=NOTHING) # type: str
    CloudFrontDefaultCertificate = attr.ib(default=NOTHING) # type: boolean
    IamCertificateId = attr.ib(default=NOTHING) # type: str
    MinimumProtocolVersion = attr.ib(default=NOTHING) # type: str
    SslSupportMethod = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.ViewerCertificate


@attr.s
class DistributionConfig(AWSObject):
    
    DefaultCacheBehavior = attr.ib() # type: DefaultCacheBehavior
    Enabled = attr.ib() # type: boolean
    Origins = attr.ib() # type: list
    Aliases = attr.ib(default=NOTHING) # type: list
    CacheBehaviors = attr.ib(default=NOTHING) # type: list
    Comment = attr.ib(default=NOTHING) # type: str
    CustomErrorResponses = attr.ib(default=NOTHING) # type: list
    DefaultRootObject = attr.ib(default=NOTHING) # type: str
    HttpVersion = attr.ib(default=NOTHING) # type: str
    IPV6Enabled = attr.ib(default=NOTHING) # type: boolean
    Logging = attr.ib(default=NOTHING) # type: Logging
    PriceClass = attr.ib(default=NOTHING) # type: priceclass_type
    Restrictions = attr.ib(default=NOTHING) # type: Restrictions
    ViewerCertificate = attr.ib(default=NOTHING) # type: ViewerCertificate
    WebACLId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.DistributionConfig


@attr.s
class Distribution(AWSObject):
    title = attr.ib()   # type: str
    
    DistributionConfig = attr.ib() # type: DistributionConfig
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.Distribution


@attr.s
class CloudFrontOriginAccessIdentityConfig(AWSObject):
    
    Comment = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.CloudFrontOriginAccessIdentityConfig


@attr.s
class CloudFrontOriginAccessIdentity(AWSObject):
    title = attr.ib()   # type: str
    
    CloudFrontOriginAccessIdentityConfig = attr.ib() # type: CloudFrontOriginAccessIdentityConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.CloudFrontOriginAccessIdentity


@attr.s
class TrustedSigners(AWSObject):
    
    Enabled = attr.ib() # type: boolean
    AwsAccountNumbers = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.TrustedSigners


@attr.s
class StreamingDistributionConfig(AWSObject):
    
    Comment = attr.ib() # type: str
    Enabled = attr.ib() # type: boolean
    S3Origin = attr.ib() # type: S3Origin
    TrustedSigners = attr.ib() # type: TrustedSigners
    Aliases = attr.ib(default=NOTHING) # type: list
    Logging = attr.ib(default=NOTHING) # type: Logging
    PriceClass = attr.ib(default=NOTHING) # type: priceclass_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.StreamingDistributionConfig


@attr.s
class StreamingDistribution(AWSObject):
    title = attr.ib()   # type: str
    
    StreamingDistributionConfig = attr.ib() # type: StreamingDistributionConfig
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudfront.StreamingDistribution
