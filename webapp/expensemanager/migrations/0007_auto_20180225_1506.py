# Generated by Django 2.0.2 on 2018-02-25 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0006_auto_20180225_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='date_time',
            new_name='pub_dat',
        ),
    ]
