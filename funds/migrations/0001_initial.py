# Generated by Django 4.0.6 on 2022-07-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('manager', models.CharField(max_length=250)),
                ('marketcap', models.CharField(max_length=250)),
            ],
        ),
    ]
