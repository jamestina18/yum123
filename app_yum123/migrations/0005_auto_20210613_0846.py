# Generated by Django 2.2 on 2021-06-13 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_yum123', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='app_yum123.User')),
                ('yelp_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yelp_review', to='app_yum123.Restau_api_obj')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
