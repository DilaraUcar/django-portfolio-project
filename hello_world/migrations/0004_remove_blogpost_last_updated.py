# Generated by Django 4.2.11 on 2024-04-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='last_updated',
        ),
    ]