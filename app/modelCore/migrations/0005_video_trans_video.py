# Generated by Django 4.2 on 2023-04-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0004_alter_video_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='trans_video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]