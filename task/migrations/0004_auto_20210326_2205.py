# Generated by Django 3.1.7 on 2021-03-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210326_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktracker',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
