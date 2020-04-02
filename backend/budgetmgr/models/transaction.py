from django.db import models
from budgetmgr.models.account import Account
from django_countries.fields import CountryField
from django.contrib.postgres.fields import ArrayField


class ExpenseType(models.Model):
    '''such as restaurant, clothes, trave, etc.'''
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Merchant(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20, blank=True)
    country = CountryField(default='US')

    def __str__(self):
        return f"{self.name}|{self.city}|{self.country}"


class Transaction(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    merchant = models.ForeignKey(Merchant, on_delete=models.DO_NOTHING)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.DO_NOTHING)
    transaction_date = models.DateField()
    coupon = models.PositiveIntegerField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    notes = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

