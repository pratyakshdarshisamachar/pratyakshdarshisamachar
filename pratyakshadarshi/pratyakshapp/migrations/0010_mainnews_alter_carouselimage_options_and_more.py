# Generated by Django 4.2 on 2024-12-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratyakshapp', '0009_carouselimage_news_videonews'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Main News Title')),
                ('image', models.ImageField(upload_to='main_news_images/', verbose_name='Main News Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Main News',
                'verbose_name_plural': 'Main News Items',
            },
        ),
        migrations.AlterModelOptions(
            name='carouselimage',
            options={'verbose_name': 'Carousel Image', 'verbose_name_plural': 'Carousel Images'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News Items'},
        ),
        migrations.AlterModelOptions(
            name='videonews',
            options={'verbose_name': 'Video News', 'verbose_name_plural': 'Video News Items'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Carousel Image Title'),
        ),
        migrations.AlterField(
            model_name='videonews',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Video News Title'),
        ),
    ]
