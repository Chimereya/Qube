# Generated by Django 4.1.2 on 2023-09-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/default_profilepic/default.jpg', upload_to='profile_pics'),
        ),
    ]
