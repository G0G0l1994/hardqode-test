# Generated by Django 4.2.10 on 2024-08-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='value',
            field=models.IntegerField(default=1000, verbose_name='Значение'),
        ),
    ]
