# Generated by Django 2.2.6 on 2020-01-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geostuff_app', '0003_auto_20191215_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
