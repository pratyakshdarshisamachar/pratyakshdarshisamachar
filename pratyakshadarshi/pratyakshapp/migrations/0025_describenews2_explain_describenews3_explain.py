# Generated by Django 4.2 on 2024-12-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0024_describenews5'),
    ]

    operations = [
        migrations.AddField(
            model_name='describenews2',
            name='explain',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='describenews3',
            name='explain',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
