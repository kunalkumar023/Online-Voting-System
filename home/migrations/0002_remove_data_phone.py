# Generated by Django 4.1.1 on 2022-12-09 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='phone',
        ),
    ]