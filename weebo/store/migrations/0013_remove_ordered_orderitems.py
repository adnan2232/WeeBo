# Generated by Django 3.1.7 on 2021-04-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210406_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordered',
            name='orderitems',
        ),
    ]
