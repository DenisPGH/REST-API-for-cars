# Generated by Django 4.0.4 on 2022-05-13 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rest', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deletedat',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='deletedat',
            name='is_deleted',
        ),
    ]
