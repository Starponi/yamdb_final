# Generated by Django 2.2.16 on 2022-05-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220514_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, to='reviews.Genre'),
        ),
    ]
