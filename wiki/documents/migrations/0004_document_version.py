# Generated by Django 3.1.1 on 2020-09-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20200917_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='version',
            field=models.BigIntegerField(default=1),
        ),
    ]
