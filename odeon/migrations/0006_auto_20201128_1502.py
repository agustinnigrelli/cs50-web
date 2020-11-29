# Generated by Django 3.1.2 on 2020-11-28 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('odeon', '0005_auto_20201128_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='listing_time',
        ),
        migrations.AddField(
            model_name='announcement',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
