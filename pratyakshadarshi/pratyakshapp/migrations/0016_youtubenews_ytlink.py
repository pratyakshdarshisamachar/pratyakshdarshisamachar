# Generated by Django 4.2 on 2024-12-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0015_bottomnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubenews',
            name='ytlink',
            field=models.URLField(null=True),
        ),
    ]
