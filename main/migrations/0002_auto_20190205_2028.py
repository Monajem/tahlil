# Generated by Django 2.1.5 on 2019-02-05 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='room_count',
            new_name='room',
        ),
    ]
