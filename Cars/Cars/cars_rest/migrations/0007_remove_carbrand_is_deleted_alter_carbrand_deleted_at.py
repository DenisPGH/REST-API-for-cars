# Generated by Django 4.0.4 on 2022-05-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rest', '0006_carbrand_is_deleted_carmodel_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbrand',
            name='is_deleted',
        ),
        migrations.AlterField(
            model_name='carbrand',
            name='deleted_at',
            field=models.DateTimeField(default=None),
        ),
    ]
