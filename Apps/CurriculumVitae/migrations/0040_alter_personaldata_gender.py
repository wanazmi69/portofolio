# Generated by Django 4.0.5 on 2023-02-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0039_alter_personaldata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='gender',
            field=models.CharField(blank=True, choices=[('男', 'Male'), ('女', 'Female')], max_length=6, null=True),
        ),
    ]
