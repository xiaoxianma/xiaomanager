from django.utils.translation import gettext_lazy as _
from django.db import models


class AccountType(models.Model):

    class Category(models.TextChoices):
        CREDIT_CARD = 'CC', _('Credit Card')
        DEBIT_CARD = 'DC', _('Debit Card')
        CASH = 'CASH', _('Cash')

    name = models.CharField(max_length=4, choices=Category.choices)


class Institution(models.Model):
    name = models.CharField(max_length=20)


class Account(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING)
    account_type = models.ForeignKey(AccountType, on_delete=models.DO_NOTHING)
    number = models.CharField(max_length=20)
    alias = models.CharField(max_length=50)


class RewardType(models.Model):
    name = models.CharField(max_length=20)


class Reward(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    reward_type = models.ForeignKey(RewardType, on_delete=models.DO_NOTHING)
    xpoints = models.PositiveIntegerField()
    start_time = models.DateField()
    end_time = models.DateField()
    description = models.TextField(blank=True)

