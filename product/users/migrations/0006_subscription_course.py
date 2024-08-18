# Generated by Django 4.2.10 on 2024-08-18 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_remove_group_members_delete_membership'),
        ('users', '0005_subscription_active_subscription_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Курс', to='courses.course'),
            preserve_default=False,
        ),
    ]
