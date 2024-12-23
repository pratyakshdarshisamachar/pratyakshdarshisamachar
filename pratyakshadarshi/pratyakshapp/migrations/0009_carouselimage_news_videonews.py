# Generated by Django 4.2 on 2024-12-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0008_remove_contactmodel_subjct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_images/', verbose_name='Carousel Image')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='News Title')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='News Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Video Title')),
                ('video', models.FileField(upload_to='news_videos/', verbose_name='Video File')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
