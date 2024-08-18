# Generated by Django 4.2.10 on 2024-08-18 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_is_active_course_price_group_free_seats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(default=None, max_length=250, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс'),
        ),
    ]