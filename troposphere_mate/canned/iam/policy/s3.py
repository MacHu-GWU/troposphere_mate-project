# -*- coding: utf-8 -*-

try:
    import typing
except:
    pass


class Resource:
    all_object = "arn:aws:s3:::*/*"
    all_bucket = "arn:aws:s3:::*"

    @classmethod
    def all_object_in_these_buckets(cls, *bucket_names):
        """
        :rtype: typing.List[str]
        """
        return [
            "arn:aws:s3:::{}/*".format(bucket_name)
            for bucket_name in bucket_names
        ]

    @classmethod
    def these_buckets(cls, *bucket_names):
        """
        :rtype: typing.List[str]
        """
        return [
            "arn:aws:s3:::{}".format(bucket_name)
            for bucket_name in bucket_names
        ]

    @classmethod
    def all_object_in_this_bucket(cls, bucket_name, prefix=""):
        """
        :type bucket_name: str
        :type prefix: str
        :rtype: typing.List[str]
        """
        return [
            "arn:aws:s3:::{}/{}*".format(bucket_name, prefix)
        ]


class Action:
    get_object_related = [
        "s3:GetObject",
        "s3:GetObjectAcl",
        "s3:GetObjectTagging",
        "s3:GetObjectTorrent",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionForReplication",
        "s3:GetObjectVersionTagging",
        "s3:GetObjectVersionTorrent",
        "s3:ListMultipartUploadParts",
    ]
    get_bucket_related = [
        "s3:GetAccelerateConfiguration",
        "s3:GetAnalyticsConfiguration",
        "s3:GetBucketAcl",
        "s3:GetBucketCORS",
        "s3:GetBucketLocation",
        "s3:GetBucketLogging",
        "s3:GetBucketNotification",
        "s3:GetBucketPolicy",
        "s3:GetBucketPolicyStatus",
        "s3:GetBucketPublicAccessBlock",
        "s3:GetBucketRequestPayment",
        "s3:GetBucketTagging",
        "s3:GetBucketVersioning",
        "s3:GetBucketWebsite",
        "s3:GetEncryptionConfiguration",
        "s3:GetInventoryConfiguration",
        "s3:GetLifecycleConfiguration",
        "s3:GetMetricsConfiguration",
        "s3:GetReplicationConfiguration",
        "s3:ListBucket",
        "s3:ListBucketByTags",
        "s3:ListBucketMultipartUploads",
        "s3:ListBucketVersions",
    ]
    put_object_related = [
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:DeleteObjectTagging",
        "s3:DeleteObjectVersion",
        "s3:DeleteObjectVersionTagging",
        "s3:GetObjectLegalHold",
        "s3:GetObjectRetention",
        "s3:PutObject",
        "s3:PutObjectLegalHold",
        "s3:PutObjectRetention",
        "s3:PutObjectTagging",
        "s3:PutObjectVersionTagging",
        "s3:ReplicateDelete",
        "s3:ReplicateObject",
        "s3:ReplicateTags",
        "s3:RestoreObject",
    ]
    put_bucket_related = [
        "s3:CreateBucket",
        "s3:DeleteBucket",
        "s3:DeleteBucketWebsite",
        "s3:GetBucketObjectLockConfiguration",
        "s3:PutAccelerateConfiguration",
        "s3:PutAnalyticsConfiguration",
        "s3:PutBucketCORS",
        "s3:PutBucketLogging",
        "s3:PutBucketNotification",
        "s3:PutBucketObjectLockConfiguration",
        "s3:PutBucketRequestPayment",
        "s3:PutBucketTagging",
        "s3:PutBucketVersioning",
        "s3:PutBucketWebsite",
        "s3:PutEncryptionConfiguration",
        "s3:PutInventoryConfiguration",
        "s3:PutLifecycleConfiguration",
        "s3:PutMetricsConfiguration",
        "s3:PutReplicationConfiguration",
    ]


class JSON:
    read_only_access_to_all_bucket = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": Action.get_object_related,
                "Resource": Resource.all_object
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": Action.get_bucket_related,
                "Resource": Resource.all_bucket
            },
            {
                "Sid": "VisualEditor2",
                "Effect": "Allow",
                "Action": [
                    "s3:GetAccountPublicAccessBlock",
                    "s3:ListAllMyBuckets",
                    "s3:ListJobs",
                    "s3:HeadBucket"
                ],
                "Resource": "*"
            }
        ]
    }

    write_access_to_all_bucket = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": Action.put_object_related,
                "Resource": Resource.all_object
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": Action.put_bucket_related,
                "Resource": Resource.all_bucket
            }
        ]
    }
