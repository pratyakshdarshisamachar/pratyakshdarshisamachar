# Generated by Django 4.2 on 2024-12-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0020_describenews2'),
    ]

    operations = [
        migrations.AddField(
            model_name='describenews2',
            name='heading',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
