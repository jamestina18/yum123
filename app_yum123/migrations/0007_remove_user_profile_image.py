# Generated by Django 2.2 on 2021-06-14 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_yum123', '0006_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
    ]
