# Generated by Django 3.1.3 on 2020-11-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_remove_directory_verificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='verificacion',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]