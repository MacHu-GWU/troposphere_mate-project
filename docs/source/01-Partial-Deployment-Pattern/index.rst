.. _partial-deployment-pattern:

Partial Deployment Pattern
==============================================================================

Usually, for big projects, there are many AWS resources and depends on each other like a chain. Here's some tips for writing super big and complex template.

1. DO NOT write a super big template and then deploy, most likely its gonna fail and it is hard to debug a big template. A better approach is to start from a template with only a few resources, and deploy. Then gradually add more resources.
2. If you already have a big template and it works, it could be challenge to update a resource in the middle of the dependency chain. I recommend to ``disable`` all dependent resources and try deploy. If it works, then continue to deploy other dependent resources.
3. To maximize reuse of your code, I recommend to parameterize your template, and partialize deploy the infrastructure. For example, you may have a template that deploys a public VPC, a private VPC, a bunch of IAM role, some EC2 instance, a auto-scaling-group, a ECS cluster, some lambda function, several S3 buckets and a RDS database, and a code pipeline for your web app. It is a nicely designed an mature architect in your organization. For other projects, you can reuse this template and choose to partially deploy part of the architect.


``troposphere_mate`` provides an api allow you to easily partially deploy your template. The idea is simple, it just automatically or manually label your Resource and remove them using label.

Here's an example template with an IAM Policy, an IAM Role and an IAM Instance Profile. The Role depends on the policy, the instance profile depends on the role. For the sample template code, take a look at https://github.com/MacHu-GWU/troposphere_mate-project/tree/master/troposphere_mate/examples/partial_deploy:

.. literalinclude:: ../../../troposphere_mate/examples/partial_deploy/cft.py
    :language: python
    :emphasize-lines: 21,44,60
    :linenos:

Here's an example of how you choose to partially deploy it:

.. literalinclude:: ../../../troposphere_mate/examples/partial_deploy/deploy.py
    :language: python
    :emphasize-lines: 14-20
    :linenos:
