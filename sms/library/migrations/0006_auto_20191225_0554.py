# Generated by Django 2.2.8 on 2019-12-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_num_ent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='book_id',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
