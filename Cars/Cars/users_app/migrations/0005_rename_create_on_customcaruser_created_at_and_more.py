# Generated by Django 4.0.4 on 2022-05-10 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_customcaruser_create_on_customcaruser_update_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customcaruser',
            old_name='CREATE_ON',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customcaruser',
            old_name='UPDATE_ON',
            new_name='updated_at',
        ),
    ]
