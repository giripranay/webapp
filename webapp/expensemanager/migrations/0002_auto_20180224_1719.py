# Generated by Django 2.0.2 on 2018-02-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='category',
        ),
        migrations.AddField(
            model_name='table',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
