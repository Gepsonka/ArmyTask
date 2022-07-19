# Generated by Django 4.0.6 on 2022-07-19 21:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarData', '0002_alter_favouritecarsmodel_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favouritecarsmodel',
            unique_together={('car_type', 'user', 'year')},
        ),
    ]