# Generated by Django 4.2 on 2024-12-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0003_uploadmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel',
            name='File',
            field=models.FileField(upload_to='usernews/'),
        ),
        migrations.AlterField(
            model_name='uploadmodel',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
