# Generated by Django 3.0.4 on 2020-04-27 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EReceipt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='price',
            new_name='total_price',
        ),
    ]