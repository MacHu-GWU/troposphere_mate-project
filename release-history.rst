.. _release_history:

Release and Version History
==============================================================================


0.0.4 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


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

