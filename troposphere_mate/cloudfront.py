# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cloudfront

from troposphere.cloudfront import (
    CacheBehavior as _CacheBehavior,
    CloudFrontOriginAccessIdentityConfig as _CloudFrontOriginAccessIdentityConfig,
    Cookies as _Cookies,
    CustomErrorResponse as _CustomErrorResponse,
    CustomOriginConfig as _CustomOriginConfig,
    DefaultCacheBehavior as _DefaultCacheBehavior,
    DistributionConfig as _DistributionConfig,
    ForwardedValues as _ForwardedValues,
    GeoRestriction as _GeoRestriction,
    LambdaFunctionAssociation as _LambdaFunctionAssociation,
    Logging as _Logging,
    Origin as _Origin,
    OriginCustomHeader as _OriginCustomHeader,
    Restrictions as _Restrictions,
    S3Origin as _S3Origin,
    S3OriginConfig as _S3OriginConfig,
    StreamingDistributionConfig as _StreamingDistributionConfig,
    Tags as _Tags,
    TrustedSigners as _TrustedSigners,
    ViewerCertificate as _ViewerCertificate,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Cookies(troposphere.cloudfront.Cookies, Mixin):
    def __init__(self,
                 title=None,
                 Forward=REQUIRED, # type: str
                 WhitelistedNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Forward=Forward,
            WhitelistedNames=WhitelistedNames,
            **kwargs
        )
        super(Cookies, self).__init__(**processed_kwargs)


class ForwardedValues(troposphere.cloudfront.ForwardedValues, Mixin):
    def __init__(self,
                 title=None,
                 QueryString=REQUIRED, # type: bool
                 Cookies=NOTHING, # type: _Cookies
                 Headers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 QueryStringCacheKeys=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueryString=QueryString,
            Cookies=Cookies,
            Headers=Headers,
            QueryStringCacheKeys=QueryStringCacheKeys,
            **kwargs
        )
        super(ForwardedValues, self).__init__(**processed_kwargs)


class LambdaFunctionAssociation(troposphere.cloudfront.LambdaFunctionAssociation, Mixin):
    def __init__(self,
                 title=None,
                 EventType=NOTHING, # type: str
                 LambdaFunctionARN=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventType=EventType,
            LambdaFunctionARN=LambdaFunctionARN,
            **kwargs
        )
        super(LambdaFunctionAssociation, self).__init__(**processed_kwargs)


class CacheBehavior(troposphere.cloudfront.CacheBehavior, Mixin):
    def __init__(self,
                 title=None,
                 ForwardedValues=REQUIRED, # type: _ForwardedValues
                 PathPattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetOriginId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ViewerProtocolPolicy=REQUIRED, # type: str
                 AllowedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CachedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Compress=NOTHING, # type: bool
                 DefaultTTL=NOTHING, # type: int
                 FieldLevelEncryptionId=NOTHING, # type: Union[str, AWSHelperFn]
                 LambdaFunctionAssociations=NOTHING, # type: List[_LambdaFunctionAssociation]
                 MaxTTL=NOTHING, # type: int
                 MinTTL=NOTHING, # type: int
                 SmoothStreaming=NOTHING, # type: bool
                 TrustedSigners=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ForwardedValues=ForwardedValues,
            PathPattern=PathPattern,
            TargetOriginId=TargetOriginId,
            ViewerProtocolPolicy=ViewerProtocolPolicy,
            AllowedMethods=AllowedMethods,
            CachedMethods=CachedMethods,
            Compress=Compress,
            DefaultTTL=DefaultTTL,
            FieldLevelEncryptionId=FieldLevelEncryptionId,
            LambdaFunctionAssociations=LambdaFunctionAssociations,
            MaxTTL=MaxTTL,
            MinTTL=MinTTL,
            SmoothStreaming=SmoothStreaming,
            TrustedSigners=TrustedSigners,
            **kwargs
        )
        super(CacheBehavior, self).__init__(**processed_kwargs)


class DefaultCacheBehavior(troposphere.cloudfront.DefaultCacheBehavior, Mixin):
    def __init__(self,
                 title=None,
                 ForwardedValues=REQUIRED, # type: _ForwardedValues
                 TargetOriginId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ViewerProtocolPolicy=REQUIRED, # type: str
                 AllowedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CachedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Compress=NOTHING, # type: bool
                 DefaultTTL=NOTHING, # type: int
                 FieldLevelEncryptionId=NOTHING, # type: Union[str, AWSHelperFn]
                 LambdaFunctionAssociations=NOTHING, # type: List[_LambdaFunctionAssociation]
                 MaxTTL=NOTHING, # type: int
                 MinTTL=NOTHING, # type: int
                 SmoothStreaming=NOTHING, # type: bool
                 TrustedSigners=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ForwardedValues=ForwardedValues,
            TargetOriginId=TargetOriginId,
            ViewerProtocolPolicy=ViewerProtocolPolicy,
            AllowedMethods=AllowedMethods,
            CachedMethods=CachedMethods,
            Compress=Compress,
            DefaultTTL=DefaultTTL,
            FieldLevelEncryptionId=FieldLevelEncryptionId,
            LambdaFunctionAssociations=LambdaFunctionAssociations,
            MaxTTL=MaxTTL,
            MinTTL=MinTTL,
            SmoothStreaming=SmoothStreaming,
            TrustedSigners=TrustedSigners,
            **kwargs
        )
        super(DefaultCacheBehavior, self).__init__(**processed_kwargs)


class S3Origin(troposphere.cloudfront.S3Origin, Mixin):
    def __init__(self,
                 title=None,
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 OriginAccessIdentity=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DomainName=DomainName,
            OriginAccessIdentity=OriginAccessIdentity,
            **kwargs
        )
        super(S3Origin, self).__init__(**processed_kwargs)


class CustomOriginConfig(troposphere.cloudfront.CustomOriginConfig, Mixin):
    def __init__(self,
                 title=None,
                 OriginProtocolPolicy=REQUIRED, # type: Union[str, AWSHelperFn]
                 HTTPPort=NOTHING, # type: int
                 HTTPSPort=NOTHING, # type: int
                 OriginKeepaliveTimeout=NOTHING, # type: int
                 OriginReadTimeout=NOTHING, # type: int
                 OriginSSLProtocols=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OriginProtocolPolicy=OriginProtocolPolicy,
            HTTPPort=HTTPPort,
            HTTPSPort=HTTPSPort,
            OriginKeepaliveTimeout=OriginKeepaliveTimeout,
            OriginReadTimeout=OriginReadTimeout,
            OriginSSLProtocols=OriginSSLProtocols,
            **kwargs
        )
        super(CustomOriginConfig, self).__init__(**processed_kwargs)


class OriginCustomHeader(troposphere.cloudfront.OriginCustomHeader, Mixin):
    def __init__(self,
                 title=None,
                 HeaderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HeaderValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HeaderName=HeaderName,
            HeaderValue=HeaderValue,
            **kwargs
        )
        super(OriginCustomHeader, self).__init__(**processed_kwargs)


class S3OriginConfig(troposphere.cloudfront.S3OriginConfig, Mixin):
    def __init__(self,
                 title=None,
                 OriginAccessIdentity=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OriginAccessIdentity=OriginAccessIdentity,
            **kwargs
        )
        super(S3OriginConfig, self).__init__(**processed_kwargs)


class Origin(troposphere.cloudfront.Origin, Mixin):
    def __init__(self,
                 title=None,
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 CustomOriginConfig=NOTHING, # type: _CustomOriginConfig
                 OriginCustomHeaders=NOTHING, # type: List[_OriginCustomHeader]
                 OriginPath=NOTHING, # type: Union[str, AWSHelperFn]
                 S3OriginConfig=NOTHING, # type: _S3OriginConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DomainName=DomainName,
            Id=Id,
            CustomOriginConfig=CustomOriginConfig,
            OriginCustomHeaders=OriginCustomHeaders,
            OriginPath=OriginPath,
            S3OriginConfig=S3OriginConfig,
            **kwargs
        )
        super(Origin, self).__init__(**processed_kwargs)


class Logging(troposphere.cloudfront.Logging, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 IncludeCookies=NOTHING, # type: bool
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            IncludeCookies=IncludeCookies,
            Prefix=Prefix,
            **kwargs
        )
        super(Logging, self).__init__(**processed_kwargs)


class CustomErrorResponse(troposphere.cloudfront.CustomErrorResponse, Mixin):
    def __init__(self,
                 title=None,
                 ErrorCode=REQUIRED, # type: int
                 ErrorCachingMinTTL=NOTHING, # type: int
                 ResponseCode=NOTHING, # type: int
                 ResponsePagePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ErrorCode=ErrorCode,
            ErrorCachingMinTTL=ErrorCachingMinTTL,
            ResponseCode=ResponseCode,
            ResponsePagePath=ResponsePagePath,
            **kwargs
        )
        super(CustomErrorResponse, self).__init__(**processed_kwargs)


class GeoRestriction(troposphere.cloudfront.GeoRestriction, Mixin):
    def __init__(self,
                 title=None,
                 RestrictionType=REQUIRED, # type: str
                 Locations=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RestrictionType=RestrictionType,
            Locations=Locations,
            **kwargs
        )
        super(GeoRestriction, self).__init__(**processed_kwargs)


class Restrictions(troposphere.cloudfront.Restrictions, Mixin):
    def __init__(self,
                 title=None,
                 GeoRestriction=REQUIRED, # type: _GeoRestriction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GeoRestriction=GeoRestriction,
            **kwargs
        )
        super(Restrictions, self).__init__(**processed_kwargs)


class ViewerCertificate(troposphere.cloudfront.ViewerCertificate, Mixin):
    def __init__(self,
                 title=None,
                 AcmCertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 CloudFrontDefaultCertificate=NOTHING, # type: bool
                 IamCertificateId=NOTHING, # type: Union[str, AWSHelperFn]
                 MinimumProtocolVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 SslSupportMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AcmCertificateArn=AcmCertificateArn,
            CloudFrontDefaultCertificate=CloudFrontDefaultCertificate,
            IamCertificateId=IamCertificateId,
            MinimumProtocolVersion=MinimumProtocolVersion,
            SslSupportMethod=SslSupportMethod,
            **kwargs
        )
        super(ViewerCertificate, self).__init__(**processed_kwargs)


class DistributionConfig(troposphere.cloudfront.DistributionConfig, Mixin):
    def __init__(self,
                 title=None,
                 DefaultCacheBehavior=REQUIRED, # type: _DefaultCacheBehavior
                 Enabled=REQUIRED, # type: bool
                 Origins=REQUIRED, # type: List[_Origin]
                 Aliases=NOTHING, # type: list
                 CacheBehaviors=NOTHING, # type: List[_CacheBehavior]
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomErrorResponses=NOTHING, # type: List[_CustomErrorResponse]
                 DefaultRootObject=NOTHING, # type: Union[str, AWSHelperFn]
                 HttpVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 IPV6Enabled=NOTHING, # type: bool
                 Logging=NOTHING, # type: _Logging
                 PriceClass=NOTHING, # type: str
                 Restrictions=NOTHING, # type: _Restrictions
                 ViewerCertificate=NOTHING, # type: _ViewerCertificate
                 WebACLId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultCacheBehavior=DefaultCacheBehavior,
            Enabled=Enabled,
            Origins=Origins,
            Aliases=Aliases,
            CacheBehaviors=CacheBehaviors,
            Comment=Comment,
            CustomErrorResponses=CustomErrorResponses,
            DefaultRootObject=DefaultRootObject,
            HttpVersion=HttpVersion,
            IPV6Enabled=IPV6Enabled,
            Logging=Logging,
            PriceClass=PriceClass,
            Restrictions=Restrictions,
            ViewerCertificate=ViewerCertificate,
            WebACLId=WebACLId,
            **kwargs
        )
        super(DistributionConfig, self).__init__(**processed_kwargs)


class Distribution(troposphere.cloudfront.Distribution, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DistributionConfig=REQUIRED, # type: _DistributionConfig
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DistributionConfig=DistributionConfig,
            Tags=Tags,
            **kwargs
        )
        super(Distribution, self).__init__(**processed_kwargs)


class CloudFrontOriginAccessIdentityConfig(troposphere.cloudfront.CloudFrontOriginAccessIdentityConfig, Mixin):
    def __init__(self,
                 title=None,
                 Comment=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Comment=Comment,
            **kwargs
        )
        super(CloudFrontOriginAccessIdentityConfig, self).__init__(**processed_kwargs)


class CloudFrontOriginAccessIdentity(troposphere.cloudfront.CloudFrontOriginAccessIdentity, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CloudFrontOriginAccessIdentityConfig=REQUIRED, # type: _CloudFrontOriginAccessIdentityConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig,
            **kwargs
        )
        super(CloudFrontOriginAccessIdentity, self).__init__(**processed_kwargs)


class TrustedSigners(troposphere.cloudfront.TrustedSigners, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 AwsAccountNumbers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            AwsAccountNumbers=AwsAccountNumbers,
            **kwargs
        )
        super(TrustedSigners, self).__init__(**processed_kwargs)


class StreamingDistributionConfig(troposphere.cloudfront.StreamingDistributionConfig, Mixin):
    def __init__(self,
                 title=None,
                 Comment=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=REQUIRED, # type: bool
                 S3Origin=REQUIRED, # type: _S3Origin
                 TrustedSigners=REQUIRED, # type: _TrustedSigners
                 Aliases=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Logging=NOTHING, # type: _Logging
                 PriceClass=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Comment=Comment,
            Enabled=Enabled,
            S3Origin=S3Origin,
            TrustedSigners=TrustedSigners,
            Aliases=Aliases,
            Logging=Logging,
            PriceClass=PriceClass,
            **kwargs
        )
        super(StreamingDistributionConfig, self).__init__(**processed_kwargs)


class StreamingDistribution(troposphere.cloudfront.StreamingDistribution, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StreamingDistributionConfig=REQUIRED, # type: _StreamingDistributionConfig
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StreamingDistributionConfig=StreamingDistributionConfig,
            Tags=Tags,
            **kwargs
        )
        super(StreamingDistribution, self).__init__(**processed_kwargs)
