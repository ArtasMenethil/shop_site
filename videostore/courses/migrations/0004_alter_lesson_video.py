# Generated by Django 4.0.6 on 2022-07-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(max_length=200, verbose_name='URL видео'),
        ),
    ]
