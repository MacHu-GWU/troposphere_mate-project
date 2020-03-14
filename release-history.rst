.. _release_history:

Release and Version History
==============================================================================


0.0.15 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.14 (2020-03-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add StackManager.delete method

**Minor Improvements**

- add ec2 launch template, elb, dynamodb, elastic cache, elastic search property attributes

**Bugfixes**

- Fix troposphere module import in aws_object.py


0.0.13 (2020-02-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- now ``Template.remove_resource`` method also removes dependent using the ``DependsOn`` attributes.
- ``Template.create_resource_type_label`` no longer to create dependent resource type label to metadata. because it confuses users.

**Minor Improvements**

- add ``Template.iter_nested_template`` method to recursively iterate nested templates.

**Bugfixes**

**Miscellaneous**

- add two best practice examples, **nested stack** and **partial deploy**.
- host doc site on readthedocs.


0.0.12 (2020-02-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- now to_dict and from_dict can successfully recovery ``Output.DependsOn`` information. Which means when you remove a Resource, it also removes the dependent Output. And you can easily serialize and deserialize it worry freely.
- tons of property method added, you can easily reference resource name, resource arn and additional return values easily. No need to lookup cloudformation document. For example: ``iam.Role.iam_role_arn``, ``iam.Role.iam_role_name``, etc ...


**Minor Improvements**

- add a metadata.py submodule, import name is ``troposphere_mate.mtdt``, it allows you to visit those constant field name used in metadata.

**Bugfixes**

**Miscellaneous**


0.0.11 (2019-11-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``StackManager`` utility class, make deploy cloudformation from troposphere_mate easy
- now ``deploy_stack`` use ``cf_client`` as first argument

**Minor Improvements**

- now canned template can be visited from ``troposhere_mate.canned...`` syntax

**Bugfixes**

- fix canned VPC template

**Miscellaneous**


0.0.10 (2019-10-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``troposphere_mate.core.canned.ServerlessConfig`` config template for AWS Lambda Serverless App
- add ``troposphere_mate.core.stack_deploy.py`` module to simplify the deployment from boto3 cloudformation api.


0.0.9 (2019-10-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- ``troposphere_mate.Template.create_resource_type_label()`` method now automatically add resource_type of DependsOn to Metadata labels field. Because usually we use Metadata labels field to batch remove resource from template. If you remove a resource, then any other resource which depends on this one should also be removed.

**Minor Improvements**

- ``troposphere_mate.AwsObject`` now support many built-in property method to allow developer to directly access Reference Intrinsic or Return Values. The idle will give you the hint of what return value you can directly use. So you don't need to lookup the cloudformation document.


0.0.8 (2019-09-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- now the template object returned by ``Template.from_dict()``, comes with troposphere_mate AWS Object, instead of raw troposphere AWS Object. on 0.0.7, dump and load will lose troposphere_mate specified features
- now the magic ``troposphere_mate.associate`` method support more than 2 aws object and more key word argument
- rewrite the AWS Object association linker class, allow it to be easily extended.
- **DROP support for Python3.4 and Python3.5**


0.0.7 (2019-09-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``Template.from_dict()`` factory method! **Now you can create troposphere_mate.Template class from dictionry now!**


0.0.6 (2019-08-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``ignore_duplicate=False`` arg in ``Template.add_parameter``, ``Template.add_output``, ``Template.add_resource``
- add ApiGateway related auto Association.


0.0.5 (2019-08-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add logical ``DependsOn`` argument to Output, allow user to define dependent AWS Resource for an Output. So the ``Template.remove_resource()`` can also remove Output that depends on this resource.
- rename ``Template.remove_resource_by_tag()`` method to ``Template.remove_resource_by_label()``.


0.0.4 (2019-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``Canned`` module.
- allow ``Canned.to_file`` dump template.
- allow ``Template.remove_resource_by_tag()`` method.

**Minor Improvements**

- add ``from troposphere_mate import Canned``


0.0.3 (2019-07-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``Template.remove_resource``, ``Template.remove_parameter``, ``Template.remove_output`` method
- add Canned Template Factory class, and canned iam and vpc


0.0.2 (2019-07-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- removed dependencies ``attrs``, now explicitly use Python __init__ syntax for the code generation.
- removed the convertion layer that transform troposphere_mate.AWSObject to troposphere.AWSObject, now **troposphere_mate.AWSObject just subclass of troposphere.AWSObject**
- Now Template and any AWSObject support ``.update_tags(dict(NAME="my-project", STAGE="dev"), overwrite=False) method to allow you apply common tags.

0.0.1 (2019-07-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Features and Improvements**

- First release
- Implement auto properties hint
- Implement auto associate / reference

**Miscellaneous**

- TODO: add support to openstack

