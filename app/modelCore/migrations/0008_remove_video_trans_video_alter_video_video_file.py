# Generated by Django 4.2 on 2023-04-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0007_gamescore_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='trans_video',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(max_length=255, upload_to='videos/'),
        ),
    ]
