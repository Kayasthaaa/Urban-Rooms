# Generated by Django 4.0.1 on 2022-02-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_room_balcony_remove_room_disabled_access_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='total_rooms',
        ),
        migrations.AlterField(
            model_name='room',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]