# Generated by Django 5.1.6 on 2025-02-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='op@gmail.com', max_length=100),
        ),
    ]
