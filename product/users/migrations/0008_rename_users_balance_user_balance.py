# Generated by Django 4.2.10 on 2024-08-19 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_balance_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='users',
            new_name='user_balance',
        ),
    ]