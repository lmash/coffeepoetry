# Generated by Django 4.2.2 on 2023-09-09 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0006_cafe_haiku_check'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cafe',
            old_name='haiku_check',
            new_name='check_for_haiku',
        ),
    ]
