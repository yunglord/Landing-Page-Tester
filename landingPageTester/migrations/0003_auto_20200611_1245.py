# Generated by Django 3.0.7 on 2020-06-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPageTester', '0002_auto_20200611_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speed',
            name='median_load_time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='speed',
            name='percentile',
            field=models.FloatField(default=0),
        ),
    ]
