# Generated by Django 2.2.7 on 2019-11-30 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0002_auto_20191129_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phy_broken_eq',
            old_name='bio_eq_id',
            new_name='phy_eq_id',
        ),
        migrations.RenameField(
            model_name='phy_broken_eq',
            old_name='bio_eq_name',
            new_name='phy_eq_name',
        ),
        migrations.RenameField(
            model_name='phy_eq',
            old_name='bio_eq_amount',
            new_name='phy_eq_amount',
        ),
        migrations.RenameField(
            model_name='phy_eq',
            old_name='bio_eq_cost',
            new_name='phy_eq_cost',
        ),
        migrations.RenameField(
            model_name='phy_eq',
            old_name='bio_eq_id',
            new_name='phy_eq_id',
        ),
        migrations.RenameField(
            model_name='phy_eq',
            old_name='bio_eq_name',
            new_name='phy_eq_name',
        ),
    ]