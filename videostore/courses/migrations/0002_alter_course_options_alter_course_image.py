# Generated by Django 4.0.6 on 2022-07-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='course_img', verbose_name='Изображение'),
        ),
    ]
