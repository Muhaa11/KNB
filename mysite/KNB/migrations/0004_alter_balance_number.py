# Generated by Django 3.2.4 on 2021-07-21 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KNB', '0003_balance_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='number',
            field=models.PositiveIntegerField(default=500),
        ),
    ]
