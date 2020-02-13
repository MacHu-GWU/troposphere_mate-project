.. _nested-stacks-pattern:

Nested Stacks Pattern
==============================================================================

Like terraform, CloudFormation is a declaration language. For complex architect, it is very easy to have a huge, complex template. **To manage complex CloudFormation template and reuse codes, you would like to break it into smaller files**. It is called ``Nested Stacks Pattern``.

HOWEVER, there are a lots of trivial and manual works to do:

1. For a ``Parameter`` that used in all of the stacks, **you have to define it MULTIPLES times and MANUALLY pass it from the master to the nested stacks** using the ``AWS::Cloudformation::Stack.Properties.Parameters`` property.
2. To reference a resource's returns-value from a nested stack, **you need to MANUALLY create a** ``Output`` and using the ``GetAtt("TheNestedStackName", "Outputs.TheOutputLogicId").

these things obviously breaks the ``DIY - DO NOT REPEAT YOURSELF`` philosophy in Python.
