# Generated by Django 4.0.5 on 2023-02-04 17:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0021_alter_personaldata_status_of_residence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=85, scale=None, size=[1920, 1080], upload_to='images/%Y/%m/%d/'),
        ),
    ]
