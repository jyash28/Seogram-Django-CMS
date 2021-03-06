# Generated by Django 3.2.8 on 2021-10-25 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20211025_1744'),
        ('myapp', '0005_blogcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myapp_contactform', serialize=False, to='cms.cmsplugin')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address ')),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contactform',
                'verbose_name_plural': 'ContactForm',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
