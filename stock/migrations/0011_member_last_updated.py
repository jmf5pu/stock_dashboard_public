# Generated by Django 3.1.1 on 2021-08-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_profile_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='last_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
