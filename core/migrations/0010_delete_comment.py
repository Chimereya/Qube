# Generated by Django 4.2.5 on 2023-10-19 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_comment_options_alter_comment_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
