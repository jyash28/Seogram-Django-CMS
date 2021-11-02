# Generated by Django 3.2.8 on 2021-10-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20211025_1744'),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicecard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myapp_servicecard', serialize=False, to='cms.cmsplugin')),
                ('plantype', models.TextField()),
                ('price', models.FloatField()),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]