# Generated by Django 3.2.8 on 2021-10-25 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20211025_1744'),
        ('myapp', '0006_contactform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contactform',
        ),
    ]
