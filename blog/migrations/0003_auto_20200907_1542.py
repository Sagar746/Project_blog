# Generated by Django 3.1.1 on 2020-09-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200907_1230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='category',
        ),
    ]