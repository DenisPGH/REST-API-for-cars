# Generated by Django 4.0.4 on 2022-05-13 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rest', '0004_deletedat_deleted_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeletedAt',
        ),
        migrations.RemoveField(
            model_name='carbrand',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='usercar',
            name='is_deleted',
        ),
    ]