# Generated by Django 4.0.4 on 2022-05-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rest', '0010_remove_usercar_is_deleted_alter_usercar_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbrand',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
