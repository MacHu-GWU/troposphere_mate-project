.. _nested-stacks-pattern:

Nested Stacks Pattern
==============================================================================

.. contents::
    :depth: 1
    :local:

Like terraform, CloudFormation is a declaration language. For complex architect, it is very easy to have a huge, complex template. **To manage complex CloudFormation template and reuse codes, you would like to break it into smaller files**. It is called ``Nested Stacks Pattern``.

HOWEVER, there are a lots of trivial and manual works to do:

1. For a ``Parameter`` that used in all of the stacks, **you have to define it MULTIPLES times and MANUALLY pass it from the master to the nested stacks** using the ``AWS::Cloudformation::Stack.Properties.Parameters`` property.
2. To reference a resource's returns-value from a nested stack, **you need to MANUALLY create a** ``Output`` and using the ``GetAtt("TheNestedStackName", "Outputs.TheOutputLogicId").

these things obviously breaks the ``DIY - DO NOT REPEAT YOURSELF`` philosophy in Python.


Best Practice
------------------------------------------------------------------------------

In this example, a 3 layers nested stack structure example is provided.

They are:

1. Iam Policy Tier
2. Iam Role Tier
3. Iam Instance Profile Tier

#2 depends on #1, #3 depends on #2. And #3 is the **master tier**.

.. raw:: html

    <script src="http://gist-it.appspot.com/https://github.com/MacHu-GWU/troposphere_mate-project/blob/master/troposphere_mate/examples/nested_stack/deploy.py"></script>
