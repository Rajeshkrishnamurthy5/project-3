# Generated by Django 2.1.4 on 2018-12-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20181217_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_order',
            name='topping_allowance',
            field=models.IntegerField(default=0),
        ),
    ]
