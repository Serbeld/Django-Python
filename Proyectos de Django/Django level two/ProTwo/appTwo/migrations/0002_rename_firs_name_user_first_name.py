# Generated by Django 3.2.5 on 2021-09-25 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]
