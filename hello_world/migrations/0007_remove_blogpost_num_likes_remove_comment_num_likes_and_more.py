# Generated by Django 4.2.11 on 2024-06-10 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0006_alter_blogpost_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='num_likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='num_likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
