# Generated by Django 3.0.4 on 2020-03-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetmgr', '0004_auto_20200308_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
