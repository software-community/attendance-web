# Generated by Django 2.1.2 on 2018-12-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181223_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='profile_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='profile_id',
            new_name='teacher',
        ),
    ]
