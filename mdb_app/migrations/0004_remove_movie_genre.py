# Generated by Django 2.2.1 on 2019-05-11 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0003_auto_20190510_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
    ]
