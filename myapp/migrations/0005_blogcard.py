# Generated by Django 3.2.8 on 2021-10-25 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20211025_1744'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('myapp', '0004_pricecard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogcard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myapp_blogcard', serialize=False, to='cms.cmsplugin')),
                ('blogtitle', models.TextField()),
                ('posteddate', models.DateTimeField()),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'BLOGCARD',
                'verbose_name_plural': 'BLOGCARD',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
