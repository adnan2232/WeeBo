# Generated by Django 3.1.7 on 2021-04-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210407_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered',
            name='orderstatus',
            field=models.CharField(choices=[('ordered', 'ORDERED'), ('packed', 'PACKED'), ('shipped', 'SHIPPED'), ('delivered', 'DELIVERED')], default='ordered', max_length=20),
        ),
    ]