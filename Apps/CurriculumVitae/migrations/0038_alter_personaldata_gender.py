# Generated by Django 4.0.5 on 2023-02-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0037_alter_languageskill_personal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='gender',
            field=models.CharField(blank=True, choices=[('男', 'Male'), ('女', 'Female')], max_length=6, null=True),
        ),
    ]
