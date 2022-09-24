# Generated by Django 4.0.3 on 2022-08-23 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='entity_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.entityrequest'),
        ),
        migrations.AddField(
            model_name='payment',
            name='individual_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.individualrequest'),
        ),
    ]