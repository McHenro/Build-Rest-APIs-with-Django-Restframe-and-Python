# Generated by Django 3.2a1 on 2022-01-19 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='update',
            new_name='updated',
        ),
    ]