# Generated by Django 4.2 on 2024-12-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0023_describenews4'),
    ]

    operations = [
        migrations.CreateModel(
            name='describenews5',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('heading', models.CharField(max_length=100, null=True)),
                ('explain', models.CharField(max_length=100)),
                ('textfornews', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'describe5tb',
            },
        ),
    ]