# Generated by Django 3.2.9 on 2021-12-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211219_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
            preserve_default=False,
        ),
    ]
