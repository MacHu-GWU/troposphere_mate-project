# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.budgets

from troposphere.budgets import BudgetData
from troposphere.budgets import CostTypes
from troposphere.budgets import Notification
from troposphere.budgets import Spend
from troposphere.budgets import TimePeriod
from troposphere.budgets import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Spend(AWSObject):
    
    Amount = attr.ib() # type: float
    Unit = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.Spend


@attr.s
class CostTypes(AWSObject):
    
    IncludeCredit = attr.ib(default=NOTHING) # type: boolean
    IncludeDiscount = attr.ib(default=NOTHING) # type: boolean
    IncludeOtherSubscription = attr.ib(default=NOTHING) # type: boolean
    IncludeRecurring = attr.ib(default=NOTHING) # type: boolean
    IncludeRefund = attr.ib(default=NOTHING) # type: boolean
    IncludeSubscription = attr.ib(default=NOTHING) # type: boolean
    IncludeSupport = attr.ib(default=NOTHING) # type: boolean
    IncludeTax = attr.ib(default=NOTHING) # type: boolean
    IncludeUpfront = attr.ib(default=NOTHING) # type: boolean
    UseAmortized = attr.ib(default=NOTHING) # type: boolean
    UseBlended = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.CostTypes


@attr.s
class TimePeriod(AWSObject):
    
    End = attr.ib(default=NOTHING) # type: str
    Start = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.TimePeriod


@attr.s
class BudgetData(AWSObject):
    
    BudgetType = attr.ib() # type: str
    TimeUnit = attr.ib() # type: str
    BudgetLimit = attr.ib(default=NOTHING) # type: Spend
    BudgetName = attr.ib(default=NOTHING) # type: str
    CostFilters = attr.ib(default=NOTHING) # type: dict
    CostTypes = attr.ib(default=NOTHING) # type: CostTypes
    TimePeriod = attr.ib(default=NOTHING) # type: TimePeriod

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.BudgetData


@attr.s
class Notification(AWSObject):
    
    ComparisonOperator = attr.ib() # type: str
    NotificationType = attr.ib() # type: str
    Threshold = attr.ib() # type: float
    ThresholdType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.Notification


@attr.s
class Subscriber(AWSObject):
    
    Address = attr.ib() # type: str
    SubscriptionType = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.Subscriber


@attr.s
class NotificationWithSubscribers(AWSObject):
    
    Notification = attr.ib() # type: Notification
    Subscribers = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.NotificationWithSubscribers


@attr.s
class Budget(AWSObject):
    title = attr.ib()   # type: str
    
    Budget = attr.ib() # type: BudgetData
    NotificationsWithSubscribers = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.budgets.Budget
