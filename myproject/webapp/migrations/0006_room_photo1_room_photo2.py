# Generated by Django 4.0.1 on 2022-03-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_room_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='room'),
        ),
        migrations.AddField(
            model_name='room',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='room'),
        ),
    ]
