# Generated by Django 3.0.1 on 2020-01-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chem_lab', '0009_chem_con_aqua'),
    ]

    operations = [
        migrations.AddField(
            model_name='chem_eq',
            name='safety',
            field=models.BooleanField(default=False),
        ),
    ]