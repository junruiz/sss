# Generated by Django 4.2.11 on 2024-04-03 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_practice_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
