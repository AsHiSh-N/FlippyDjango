# Generated by Django 3.1.6 on 2021-08-09 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210809_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='card',
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.deck'),
        ),
    ]
