# Generated by Django 3.1.1 on 2021-07-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
