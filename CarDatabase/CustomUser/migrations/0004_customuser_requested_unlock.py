# Generated by Django 4.0.6 on 2022-07-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0003_customuser_requested_delete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='requested_unlock',
            field=models.BooleanField(default=False),
        ),
    ]