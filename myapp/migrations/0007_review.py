# Generated by Django 3.2a1 on 2022-01-13 18:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_watchlist_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='myapp.watchlist', verbose_name='Watchlist')),
            ],
        ),
    ]
