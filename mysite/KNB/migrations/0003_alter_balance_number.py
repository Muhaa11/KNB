# Generated by Django 3.2.5 on 2021-07-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KNB', '0002_balance_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='number',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]