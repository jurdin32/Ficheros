# Generated by Django 3.1.3 on 2020-11-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_directory_verificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='verificacion',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
