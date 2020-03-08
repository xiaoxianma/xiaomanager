# Generated by Django 3.0.4 on 2020-03-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetmgr', '0003_auto_20200308_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='name',
            field=models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card'), ('CASH', 'Cash'), ('CK', 'Checking'), ('SA', 'Saving')], max_length=4, unique=True),
        ),
    ]
