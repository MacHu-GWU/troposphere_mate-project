.. image:: https://readthedocs.org/projects/troposphere_mate/badge/?version=latest
    :target: https://troposphere_mate.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://travis-ci.org/MacHu-GWU/troposphere_mate-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/troposphere_mate-project?branch=master

.. image:: https://codecov.io/gh/MacHu-GWU/troposphere_mate-project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/MacHu-GWU/troposphere_mate-project

.. image:: https://img.shields.io/pypi/v/troposphere_mate.svg
    :target: https://pypi.python.org/pypi/troposphere_mate

.. image:: https://img.shields.io/pypi/l/troposphere_mate.svg
    :target: https://pypi.python.org/pypi/troposphere_mate

.. image:: https://img.shields.io/pypi/pyversions/troposphere_mate.svg
    :target: https://pypi.python.org/pypi/troposphere_mate

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/troposphere_mate-project

------


.. image:: https://img.shields.io/badge/Link-Document-blue.svg
      :target: https://troposphere_mate.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
      :target: https://troposphere_mate.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
      :target: https://troposphere_mate.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
      :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/troposphere_mate-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: https://github.com/MacHu-GWU/troposphere_mate-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: https://github.com/MacHu-GWU/troposphere_mate-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.org/pypi/troposphere_mate#files


Welcome to ``troposphere_mate`` Documentation
==============================================================================

``troposphere_mate`` is **a productive Pythonic Cloudformation Orchestration Tool**.

.. contents::
    :depth: 1
    :local:

`troposphere <https://github.com/cloudtools/troposphere>`_ is a great Python library allow you to define AWS CloudFormation Resource in Python Class. **But due to its implementation, IDLE can't use attribute auto hint, and Type hint doesn't work as well**. 

``troposphere_mate`` provides **API exactly same as** ``troposphere``, and comes with **Properties auto hint** and **type hint**. ``troposphere_mate`` is just a thin wrapper layer on top of ``troposphere``. Any ``troposphere_mate.AWSObject`` is just subclass of ``troposphere.AWSObject``.

My goal is 100% API compatible to ``troposphere``. Basically, you just need to replace ``from troposphere import Template, Ref, Tags, GetAtt`` to ``from troposphere_mate import Template, Ref, Tags, GetAtt``.

**Here's how it looks like in IDLE**:

.. image:: https://user-images.githubusercontent.com/6800411/60903484-686b1b80-a23f-11e9-8d20-22c989339cd0.png
    :width: 600 px

.. image:: https://user-images.githubusercontent.com/6800411/60776028-e40d8100-a0f6-11e9-9cae-98af25cbd9b7.png
    :width: 600 px

.. image:: https://user-images.githubusercontent.com/6800411/60776079-3484de80-a0f7-11e9-81b8-c4b2f1c4b45e.png
    :width: 600 px

Of course you can do:

.. code-block:: python

    ec2 = ec2.Instance(
        title="MyEc2Instance),
        InstanceType="t2.micro",
        Tags=Tags(
            Creator="MyName",
            Name="PlayGround",
        ),
        ...
    )

How ``troposphere`` implements:

.. code-block:: python

    # content of troposphere.ec2.py
    class Instance(AWSObject):
        resource_type = "AWS::EC2::Instance"

        props = {
            'InstanceType': (basestring, False),
            'SubnetId': (basestring, False),
            'KeyName': (basestring, False),
            ...
        }

How ``troposphere_mate`` implements:

.. code-block:: python

    # content of troposphere_mate.ec2.py
    class Instance(troposphere.ec2.Instance, Mixin):
        def __init__(self,
                     title, # type: str
                     template=None, # type: Template
                     validation=True, # type: bool
                     InstanceType=NOTHING, # type: str
                     SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                     KeyName=NOTHING, # type: Union[str, AWSHelperFn]
                     ...
                     **kwargs):
            ...


Additional Powerful Features
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:


Batch Tagging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you want to **apply a set of common tags to all AWS Resource** defined in a Template. ``trpoosphere_mate`` allows you to:

- apply common tags to specified list of AWS Resource or all of Resources in a Template.
- custom tag creation logic function, let's say based on the Resource Type.
- allow you to choose the merge ``existing tag`` into ``common tag`` or reversely.

Example:

.. code-block:: python

    from troposphere_mate import Template, ec2, Tags,
    from functools import partial

    tpl = Template()

    my_vpc = ec2.VPC(
        "MyVPC",
        template=tpl,
        CidrBlock="10.0.0.0/16",
        Tags=Tags(
            Creator="Alice"
        )
    )
    my_sg = ec2.SecurityGroup(
        "MySG",
        template=tpl,
        GroupDescription="My",
        GroupName="MySG",
        VpcId=Ref(my_vpc),
    )
    my_subnet = ec2.Subnet(
        "MySubnet",
        template=tpl,
        CidrBlock="10.0.1.0/24",
        VpcId=Ref(my_vpc),
    )

    # custom logic to create tag if it is a SecurityGroup
    def get_name(resource, project):
        if resource.resource_type == "AWS::EC2::SecurityGroup":
            return "{}/sg/{}".format(project, resource.GroupName)

    common_tags = dict(
        Project="my-project",
        Name=functools.partial(get_name, project="my-project"),
        Creator="Bob",
    )

    # apply common tags to all aws resource
    tpl.update_tags(common_tags, overwrite=False)

    assert tags_list_to_dct(tpl.to_dict()["Resources"]["MyVPC"]["Properties"]["Tags"]) == dict(
        Project="my-project",
        Creator="Alice",
    )
    assert tags_list_to_dct(tpl.to_dict()["Resources"]["MySG"]["Properties"]["Tags"]) == dict(
        Project="my-project",
        Name="my-project/sg/MySG",
        Creator="Bob",
    )

Any AWS Resource object and Template object has a utility method ``.update_tags()``

.. code-block:: python

    # by default overwrite = False, so common tags doesn't overwrite existing tags
    # update single resource
    my_ec2.update_tags({"Project": "my-project"})
    # update entire template
    tpl.update_taggs({"Project": "my-project"})


Auto Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, you just know you need to associate one AWS Resource to another, but you
have to lookup the Document to find out which Property and what is the Syntax to do that.

For example, **if you want to associate an IAM Role, VPC Subnet, Security Group to a Lambda Function**.

Suppose you already have:

.. code-block:: python

    from troposphere_mate import ec2, awslambda, iam

    tpl = Template()

    iam_role = iam.Role(
        title="MyIamRole",
        template=tpl,
        RoleName="lambda-basic-execution",
        AssumeRolePolicyDocument={},
    )

    vpc = ec2.VPC(
        title="MyVPC",
        template=tpl,
        CidrBlock="10.53.0.0/16"
    )

    public_subnet1 = ec2.Subnet(
        title="PublicSubnet1",
        template=tpl,
        CidrBlock="10.53.0.0/16",
        VpcId=Ref(vpc)
    )
    public_subnet2 = ec2.Subnet(
        title="PublicSubnet2",
        template=tpl,
        CidrBlock="10.53.2.0/16",
        VpcId=Ref(vpc)
    )

    sg = ec2.SecurityGroup(
        title="LambdaSG",
        template=tpl,
        GroupDescription="Just a SG"
    )

    lbd_func = awslambda.Function(
        title="MyFunc",
        template=tpl,
        Code=awslambda.Code(
            S3Bucket="my-bucket",
            S3Key="0.0.1.zip",
        ),
        Handler="my_func.handler",
        Role="arn:aws:iam::111122223333:role/todo",
        Runtime="python3.6"
    )


With ``troposphere_mate``, you just need to do this:

.. code-block:: python

    from troposphere_mate import associate

    associate(lbd_func, iam_role) # order doesn't matter, associate(iam_role, lbd_func)
    associate(lbd_func, sg)
    associate(lbd_func, public_subnet1)
    associate(lbd_func, public_subnet2)

In other word, you don't need to remember the properties and the syntax.

.. code-block:: python

    from troposphere import Ref
    from troposphere import awslambda

    lbd_func.Role = Ref(iam_role)
    lbd_func.VpcConfig = awslambda.VPCConfig(
        SecurityGroupIds=[
            Ref(sg)
        ],
        SubnetIds=[
            Ref(public_subnet1),
            Ref(public_subnet2),
        ]
    )

If you want to contribute your auto-associate logic to ``troposphere_mate``, please submit `issue <https://github.com/MacHu-GWU/troposphere_mate-project/issues>`_ or help me to improve. Here's an `example <https://github.com/MacHu-GWU/troposphere_mate-project/blob/master/troposphere_mate/core/associate.py>`_.


Partial Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At most of the times, eventually your cloudformation template becomes very big. There are some common use case in development and deployment:

1. **You want to reuse the AWS Resource from an Big Architect Design, only deploy selected AWS Resource, without editing the template.**
2. **You want to gradually deploy AWS Resource instead of deploy everything in one command, while you are doing development or debugging, without editing the template.**

`troposphere_mate <https://github.com/MacHu-GWU/troposphere_mate-project>`_ **allows you to define labels for your AWS Resource** in ``Metadata`` field, then you can use ``Template.remove_resource_by_label(label="a label", label_field_in_metadata="labels")`` method to **batch remove AWS Resource from your template**.

More importantly, `troposphere_mate <https://github.com/MacHu-GWU/troposphere_mate-project>`_ **allows you to explicitly defines dependent AWS Resource for Output object, so when you remove the resource, related output will automatically removed**, which is not supported by native CloudFormation or ``troposphere``.

Example:

.. code-block:: python

    from troposphere_mate import ec2, rds

    class Labels:
        tier1_vpc = "tier1_vpc"
        vpc = "vpc"
        sg = "security_group"
        tier2_rds = "tier2_rds"
        db_subnet_group = "db_subnet_group"
        db_instance = "db_instance"

    tpl = Template()

    vpc = ec2.VPC(
        "VPC",
        template=tpl,
        Metadata={"labels": [Labels.tier1_vpc, Labels.vpc]},
        ...
    )

    sg_ssh = ec2.SecurityGroup(
        "SecurityGroupSSH",
        template=tpl,
        Metadata={"labels": [Labels.tier1_vpc, Labels.sg]},
        ...
    )

    rds_db_subnet_group = rds.DBSubnetGroup(
        "DBInstance",
        template=tpl,
        Metadata={"labels": [Labels.tier2_rds, Labels.db_subnet_group]}
    )

    rds_instance = rds.DBInstance(
        "DBInstance",
        template=tpl,
        Metadata={"labels": [Labels.tier2_rds, Labels.db_instance]}
    )

    tpl.add_output(
        Output(
            "VPC",
            Description="VPC ID",
            Value=Ref(vpc),
            Export=Export("vpc-id")),
            DependsOn=[vpc,], # specify the dependent AWS Resource, so when you remove the resource, related output will automatically removed
        ),
    )

    assert len(tpl.resources) == 4
    assert len(tpl.outputs) == 1

    tpl.remove_resource_by_label(Labels.db_instance)
    assert len(tpl.resources) == 3

    tpl.remove_resource_by_label(Labels.tier2_rds)
    assert len(tpl.resources) == 2

    tpl.remove_resource_by_label(Labels.tier1_vpc)
    assert len(tpl.resources) == 0
    assert len(tpl.outputs) == 0


.. _install:

Install
------------------------------------------------------------------------------

``troposphere_mate`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install troposphere_mate

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade troposphere_mate