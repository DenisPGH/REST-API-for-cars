# Generated by Django 4.0.4 on 2022-05-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rest', '0005_delete_deletedat_remove_carbrand_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbrand',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usercar',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
