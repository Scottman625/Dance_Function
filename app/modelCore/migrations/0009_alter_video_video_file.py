# Generated by Django 4.2 on 2023-04-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0008_remove_video_trans_video_alter_video_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
