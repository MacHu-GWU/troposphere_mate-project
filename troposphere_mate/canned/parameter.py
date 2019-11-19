# -*- coding: utf-8 -*-

from troposphere_mate import Parameter

param_project_name = Parameter(
    "ProjectName",
    Type="String",
    Description=(
        "the sluggified project name, please make it as short as possible"
    ),
    MaxLength=32,
    Default="my-project",
)

param_stage = Parameter(
    "Stage",
    Type="String",
    Description=(
        "an stage name indicate the which environment of this project the "
        "application running on."
    ),
    AllowedValues=["dev", "test", "stage", "qa", "prod", "temp"],
    MaxLength=32,
    Default="dev"
)

param_env_name = Parameter(
    "EnvironmentName",
    Type="String",
    Description=(
        "an environment name includes the slugified project name and stage name, "
        "represent the environment tag, and it will be a global resource name "
        "prefix for all AWS Resource. For example: "
        "my-project-dev-iam-role, my-project-dev-s3-bucket"
    ),
    MaxLength=32,
    Default="my-project-dev"
)
