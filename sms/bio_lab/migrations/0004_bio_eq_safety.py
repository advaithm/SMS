# Generated by Django 3.0.1 on 2020-01-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio_lab', '0003_auto_20191129_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio_eq',
            name='safety',
            field=models.BooleanField(default=False),
        ),
    ]