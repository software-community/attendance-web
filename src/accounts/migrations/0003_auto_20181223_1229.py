# Generated by Django 2.1.2 on 2018-12-23 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181025_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student',
            new_name='profile_id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher',
            new_name='profile_id',
        ),
    ]
