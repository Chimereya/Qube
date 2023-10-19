# Generated by Django 4.1.2 on 2023-09-08 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='static/default_profilepic/default.png', upload_to='profile_pics')),
                ('website_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]