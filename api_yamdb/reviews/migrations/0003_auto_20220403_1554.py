# Generated by Django 2.2.19 on 2022-04-03 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211115_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]