# Generated by Django 3.2.5 on 2021-08-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210813_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
