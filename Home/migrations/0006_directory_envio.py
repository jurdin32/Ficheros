# Generated by Django 3.1.3 on 2020-11-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_directory_verificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='envio',
            field=models.BooleanField(default=False),
        ),
    ]