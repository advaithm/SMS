# Generated by Django 3.0.1 on 2020-01-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chem_lab', '0008_chem_con_reo'),
    ]

    operations = [
        migrations.AddField(
            model_name='chem_con',
            name='aqua',
            field=models.BooleanField(default=False),
        ),
    ]
