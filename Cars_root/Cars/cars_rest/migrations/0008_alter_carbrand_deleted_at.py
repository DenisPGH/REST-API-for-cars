# Generated by Django 4.0.4 on 2022-05-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rest', '0007_remove_carbrand_is_deleted_alter_carbrand_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbrand',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
