from django.utils.translation import gettext_lazy as _
from django.db import models


class AccountType(models.Model):

    class Category(models.TextChoices):
        CREDIT_CARD = 'CC', _('Credit Card')
        DEBIT_CARD = 'DC', _('Debit Card')
        CASH = 'CASH', _('Cash')
        CHECKING = 'CK', _('Checking')
        SAVING = 'SA', _('Saving')

    name = models.CharField(max_length=4, choices=Category.choices, unique=True)

    def __str__(self):
        return self.get_name_display()


class Institution(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING)
    account_type = models.ForeignKey(AccountType, on_delete=models.DO_NOTHING)
    owner = models.CharField(max_length=10, null=True)
    number = models.CharField(max_length=20, unique=True)
    alias = models.CharField(max_length=50, unique=True)

    def __str__(self):
        ret = f'{self.institution}|{self.account_type}|{self.owner}'
        if self.alias:
            ret = f'{ret}|{self.alias}'
        return ret


class RewardType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Reward(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    reward_type = models.ForeignKey(RewardType, on_delete=models.DO_NOTHING)
    xpoints = models.PositiveIntegerField()
    start_time = models.DateField()
    end_time = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        if self.end_time:
            active_period = 'TBD'
        else:
            active_period = "4ever"
        return f"{self.account}|{active_period}|{self.reward_type}"
