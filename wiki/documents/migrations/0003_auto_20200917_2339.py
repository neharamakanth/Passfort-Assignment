# Generated by Django 3.1.1 on 2020-09-17 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20200917_2324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={},
        ),
        migrations.RenameField(
            model_name='document',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='timestamp',
            new_name='created_timestamp',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='updated',
            new_name='modified_timestamp',
        ),
    ]
