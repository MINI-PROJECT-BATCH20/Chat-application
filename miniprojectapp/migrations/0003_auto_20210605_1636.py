# Generated by Django 3.2.4 on 2021-06-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniprojectapp', '0002_auto_20210605_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='user_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
