# Generated by Django 3.2a1 on 2022-01-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220105_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='website',
            field=models.URLField(max_length=100, verbose_name='Website'),
        ),
    ]
