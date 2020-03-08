from django.db import models
from budgetmgr.models.account import Account, Reward
from django_countries.fields import CountryField
from django.contrib.postgres.fields import ArrayField


class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    reward = models.ForeignKey(Reward, on_delete=models.DO_NOTHING)


class ExpenseType(models.Model):
    '''such as restaurant, clothes, trave, etc.'''
    name = models.CharField(max_length=20)


class Merchant(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20, blank=True)
    country = CountryField(default='US')


class Transaction(models.Model):
    amount = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.DO_NOTHING)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.DO_NOTHING)
    transaction_date = models.DateField()
    coupon = models.PositiveIntegerField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    notes = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

