# Generated by Django 4.0.4 on 2022-09-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_remove_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]