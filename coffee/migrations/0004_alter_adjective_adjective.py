# Generated by Django 4.2.2 on 2023-09-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_create_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjective',
            name='adjective',
            field=models.TextField(max_length=60),
        ),
    ]