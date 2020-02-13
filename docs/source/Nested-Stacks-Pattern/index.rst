.. _nested-stacks-pattern:

Nested Stacks Pattern
==============================================================================

.. contents::
    :depth: 1
    :local:

Like terraform, CloudFormation is a declaration language. For complex architect, it is very easy to have a huge, complex template. **To manage complex CloudFormation template and reuse codes, you would like to break it into smaller files**. It is called ``Nested Stacks Pattern``.

HOWEVER, there are a lots of trivial and manual works to do:

1. For a ``Parameter`` that used in all of the stacks, **you have to define it MULTIPLES times and MANUALLY pass it from the master to the nested stacks** using the ``AWS::Cloudformation::Stack.Properties.Parameters`` property.
2. To reference a resource's returns-value from a nested stack, **you need to MANUALLY create a** ``Output`` and using the ``GetAtt("TheNestedStackName", "Outputs.TheOutputLogicId")``.

these things obviously breaks the ``DIY - DO NOT REPEAT YOURSELF`` philosophy in Python.


.. _nested-stacks-pattern-best-practice:

Best Practice
------------------------------------------------------------------------------

In this example, a three layers nested stack structure example is provided.

They are:

1. Iam Policy Tier
2. Iam Role Tier
3. Iam Instance Profile Tier

#2 depends on #1, #3 depends on #2. And #3 is the **master tier**.

1. **IAM Policy Tier**:

.. literalinclude:: ../../../troposphere_mate/examples/nested_stack/tier_1_1_iam_policy.py
    :language: python
    :emphasize-lines: 4,39
    :linenos:

2. **IAM Role Tier**:

.. literalinclude:: ../../../troposphere_mate/examples/nested_stack/tier_1_iam_role.py
    :language: python
    :emphasize-lines: 4,12-15,31,36,46,53
    :linenos:

3. **IAM Instance Profile Tier**:

.. literalinclude:: ../../../troposphere_mate/examples/nested_stack/tier_master_iam_inst_profile.py
    :language: python
    :emphasize-lines: 4,13-16,32,37,44
    :linenos:

4. **The deploy script**:

.. literalinclude:: ../../../troposphere_mate/examples/nested_stack/deploy.py
    :language: python
    :linenos:

Why this is good?

1. **Deploy nested stacks made easy via Python**. Manipulating parameters and tags is hard in shell, it's not easy to implement the deployment script right and integrate with your parameter stores and CI/CD system. See the **deploy script**.
2. **Parameter and Output reference made easy**. For raw cloudformation template, no IDE will tell you the exact logic id of a parameter or output. Even in terraform, it just gives you syntax highlight but not prevent you from typing wrong. Since ``troposphere_mate`` is python, everything is an object, you can easily import and reference.
3. **Manage complex project made easy**. Since everything is just python object, you can easily break it done to different module and class. And create any custom pre processing / post processing logic.
