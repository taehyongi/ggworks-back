# Generated by Django 2.1.2 on 2018-11-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ggworks_api', '0007_auto_20181118_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo_small',
            field=models.BinaryField(blank=True),
        ),
    ]
