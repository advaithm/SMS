# Generated by Django 2.2.8 on 2019-12-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_mass_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='num_ent',
            fields=[
                ('ISBN', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
