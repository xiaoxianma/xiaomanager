# Generated by Django 3.0.4 on 2020-03-08 16:31

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('alias', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card'), ('CASH', 'Cash')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', django_countries.fields.CountryField(default='US', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.Account')),
            ],
        ),
        migrations.CreateModel(
            name='RewardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('transaction_date', models.DateField()),
                ('coupon', models.PositiveIntegerField(blank=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, null=True, size=None)),
                ('notes', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('expense_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.ExpenseType')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.Merchant')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetmgr.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xpoints', models.PositiveIntegerField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.Account')),
                ('reward_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.RewardType')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.Reward'),
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.AccountType'),
        ),
        migrations.AddField(
            model_name='account',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='budgetmgr.Institution'),
        ),
    ]
