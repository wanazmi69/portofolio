# Generated by Django 4.0.5 on 2023-02-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0025_alter_personaldata_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='hobbie',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
