# Generated by Django 3.1.1 on 2021-07-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20210719_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='assets',
            field=models.ManyToManyField(blank=True, to='stock.Asset'),
        ),
    ]
