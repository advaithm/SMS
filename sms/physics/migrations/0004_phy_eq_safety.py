# Generated by Django 3.0.1 on 2020-01-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0003_auto_20191130_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='phy_eq',
            name='safety',
            field=models.BooleanField(default=False),
        ),
    ]
