# Generated by Django 3.1.6 on 2021-08-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210816_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='back',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='front',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]