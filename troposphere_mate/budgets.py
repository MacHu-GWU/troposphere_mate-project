# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.budgets

from troposphere.budgets import (
    BudgetData as _BudgetData,
    CostTypes as _CostTypes,
    Notification as _Notification,
    NotificationWithSubscribers as _NotificationWithSubscribers,
    Spend as _Spend,
    Subscriber as _Subscriber,
    TimePeriod as _TimePeriod,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Spend(troposphere.budgets.Spend, Mixin):
    def __init__(self,
                 title=None,
                 Amount=REQUIRED, # type: float
                 Unit=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Amount=Amount,
            Unit=Unit,
            **kwargs
        )
        super(Spend, self).__init__(**processed_kwargs)


class CostTypes(troposphere.budgets.CostTypes, Mixin):
    def __init__(self,
                 title=None,
                 IncludeCredit=NOTHING, # type: bool
                 IncludeDiscount=NOTHING, # type: bool
                 IncludeOtherSubscription=NOTHING, # type: bool
                 IncludeRecurring=NOTHING, # type: bool
                 IncludeRefund=NOTHING, # type: bool
                 IncludeSubscription=NOTHING, # type: bool
                 IncludeSupport=NOTHING, # type: bool
                 IncludeTax=NOTHING, # type: bool
                 IncludeUpfront=NOTHING, # type: bool
                 UseAmortized=NOTHING, # type: bool
                 UseBlended=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IncludeCredit=IncludeCredit,
            IncludeDiscount=IncludeDiscount,
            IncludeOtherSubscription=IncludeOtherSubscription,
            IncludeRecurring=IncludeRecurring,
            IncludeRefund=IncludeRefund,
            IncludeSubscription=IncludeSubscription,
            IncludeSupport=IncludeSupport,
            IncludeTax=IncludeTax,
            IncludeUpfront=IncludeUpfront,
            UseAmortized=UseAmortized,
            UseBlended=UseBlended,
            **kwargs
        )
        super(CostTypes, self).__init__(**processed_kwargs)


class TimePeriod(troposphere.budgets.TimePeriod, Mixin):
    def __init__(self,
                 title=None,
                 End=NOTHING, # type: Union[str, AWSHelperFn]
                 Start=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            End=End,
            Start=Start,
            **kwargs
        )
        super(TimePeriod, self).__init__(**processed_kwargs)


class BudgetData(troposphere.budgets.BudgetData, Mixin):
    def __init__(self,
                 title=None,
                 BudgetType=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeUnit=REQUIRED, # type: Union[str, AWSHelperFn]
                 BudgetLimit=NOTHING, # type: _Spend
                 BudgetName=NOTHING, # type: Union[str, AWSHelperFn]
                 CostFilters=NOTHING, # type: dict
                 CostTypes=NOTHING, # type: _CostTypes
                 TimePeriod=NOTHING, # type: _TimePeriod
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BudgetType=BudgetType,
            TimeUnit=TimeUnit,
            BudgetLimit=BudgetLimit,
            BudgetName=BudgetName,
            CostFilters=CostFilters,
            CostTypes=CostTypes,
            TimePeriod=TimePeriod,
            **kwargs
        )
        super(BudgetData, self).__init__(**processed_kwargs)


class Notification(troposphere.budgets.Notification, Mixin):
    def __init__(self,
                 title=None,
                 ComparisonOperator=REQUIRED, # type: Union[str, AWSHelperFn]
                 NotificationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Threshold=REQUIRED, # type: float
                 ThresholdType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComparisonOperator=ComparisonOperator,
            NotificationType=NotificationType,
            Threshold=Threshold,
            ThresholdType=ThresholdType,
            **kwargs
        )
        super(Notification, self).__init__(**processed_kwargs)


class Subscriber(troposphere.budgets.Subscriber, Mixin):
    def __init__(self,
                 title=None,
                 Address=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubscriptionType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Address=Address,
            SubscriptionType=SubscriptionType,
            **kwargs
        )
        super(Subscriber, self).__init__(**processed_kwargs)


class NotificationWithSubscribers(troposphere.budgets.NotificationWithSubscribers, Mixin):
    def __init__(self,
                 title=None,
                 Notification=REQUIRED, # type: _Notification
                 Subscribers=REQUIRED, # type: List[_Subscriber]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Notification=Notification,
            Subscribers=Subscribers,
            **kwargs
        )
        super(NotificationWithSubscribers, self).__init__(**processed_kwargs)


class Budget(troposphere.budgets.Budget, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Budget=REQUIRED, # type: _BudgetData
                 NotificationsWithSubscribers=NOTHING, # type: List[_NotificationWithSubscribers]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Budget=Budget,
            NotificationsWithSubscribers=NotificationsWithSubscribers,
            **kwargs
        )
        super(Budget, self).__init__(**processed_kwargs)
