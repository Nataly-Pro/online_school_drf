# Generated by Django 5.0 on 2023-12-18 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_lesson_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('course', 'id'), 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
