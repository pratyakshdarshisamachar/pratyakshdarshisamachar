# Generated by Django 4.2 on 2024-12-17 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0010_mainnews_alter_carouselimage_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarouselImage',
        ),
        migrations.DeleteModel(
            name='MainNews',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='VideoNews',
        ),
    ]