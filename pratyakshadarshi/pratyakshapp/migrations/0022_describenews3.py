# Generated by Django 4.2 on 2024-12-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0021_describenews2_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='describenews3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('heading', models.CharField(max_length=100, null=True)),
                ('textfornews', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'describe3tb',
            },
        ),
    ]
