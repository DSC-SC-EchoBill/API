# Generated by Django 3.0.4 on 2020-03-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EReceipt', '0002_auto_20200315_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=6, null=True, verbose_name='birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=16, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=16, unique=True, verbose_name='id'),
        ),
    ]