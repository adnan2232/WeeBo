# Generated by Django 3.1.7 on 2021-03-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210313_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
