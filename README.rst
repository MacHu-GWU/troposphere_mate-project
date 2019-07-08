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

`troposphere <https://github.com/cloudtools/troposphere>`_ is a great Python library allow you to define AWS CloudFormation Resource in Python Class. **But due to its implementation, IDLE can't use attribute auto hint, and Type hint doesn't work as well**. ``troposphere_mate`` provides API exactly same as ``troposphere``, but with availalbe Properties auto hint feature and type hint enabled. ``troposphere_mate`` is a thin wrapper layer on top of ``troposphere``.

My goal is 100% API compatible to ``troposphere``. Basically, you just need to replace ``from troposphere import Template, Ref, Tags, GetAtt`` to ``from troposphere_mate import Template, Ref, Tags, GetAtt``.

Here's how it looks like in IDLE:

.. image:: https://user-images.githubusercontent.com/6800411/60776028-e40d8100-a0f6-11e9-9cae-98af25cbd9b7.png

.. image:: https://user-images.githubusercontent.com/6800411/60776079-3484de80-a0f7-11e9-81b8-c4b2f1c4b45e.png

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

    @attr.s
    class Instance(AWSObject):
        title = attr.ib() # type: str

        InstanceType = attr.ib(default=NOTHING) # type: str
        SubnetId = attr.ib(default=NOTHING) # type: str
        KeyName = attr.ib(default=NOTHING) # type: str

        template = attr.ib(default=None) # type: Template
        validation = attr.ib(default=True) # type: bool

        _aws_object_class = troposphere.ec2.Instance


**ATTENTION!**:

    **If you have updated the AWSObject after creation, You have to call** ``xxx.update_aws_object()`` **method to reflect the change to the real** ``troposphere.AWSObject``. Otherwise, the template will not generate the desired json for you.

    Example::

        from troposphere_mate import iam

        my_role = iam.Role(title="MyRole")
        my_role.RoleName = "my-role"
        my_role.update_aws_object()


Additional Features
------------------------------------------------------------------------------


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


.. _install:

Install
------------------------------------------------------------------------------

``troposphere_mate`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install troposphere_mate

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade troposphere_mate