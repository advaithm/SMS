# Generated by Django 3.0.1 on 2020-01-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0003_super_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
