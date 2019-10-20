# Generated by Django 2.2.6 on 2019-10-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0005_auto_20181104_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_type',
            field=models.CharField(choices=[('lecture', 'Lecture'), ('lab', 'Lab'), ('tutorial', 'Tutorial')], max_length=10, null=True),
        ),
    ]
