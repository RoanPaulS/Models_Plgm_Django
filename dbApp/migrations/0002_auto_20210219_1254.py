# Generated by Django 3.1.6 on 2021-02-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empAddress',
            field=models.CharField(max_length=100),
        ),
    ]
