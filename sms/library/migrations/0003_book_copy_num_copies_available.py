# Generated by Django 2.2.7 on 2019-12-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_book_copy_copies_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_copy',
            name='num_copies_available',
            field=models.PositiveIntegerField(default=1),
        ),
    ]