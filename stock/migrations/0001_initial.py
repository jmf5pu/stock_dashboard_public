# Generated by Django 3.1.1 on 2021-07-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=8)),
                ('pe_ratio', models.FloatField(null=True)),
                ('eps', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['ticker'],
            },
        ),
    ]