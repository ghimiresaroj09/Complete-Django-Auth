# Generated by Django 5.1 on 2024-11-06 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customuser_otp_customuser_otp_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp_expiration',
        ),
    ]
