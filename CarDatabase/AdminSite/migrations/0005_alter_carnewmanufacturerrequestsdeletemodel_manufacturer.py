# Generated by Django 4.0.6 on 2022-07-21 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarData', '0007_alter_favouritecarsmodel_fuel'),
        ('AdminSite', '0004_alter_carnewmanufacturerrequestsdeletemodel_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnewmanufacturerrequestsdeletemodel',
            name='manufacturer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CarData.manufacturernamesmodel'),
        ),
    ]
