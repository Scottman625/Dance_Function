# Generated by Django 4.2 on 2023-04-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
