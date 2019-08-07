.. _release_history:

Release and Version History
==============================================================================


0.0.6 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


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

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.1 (2019-07-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Features and Improvements**

- First release
- Implement auto properties hint
- Implement auto associate / reference

**Miscellaneous**

- TODO: add support to openstack

