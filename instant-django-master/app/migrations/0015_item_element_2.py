# Generated by Django 2.1.2 on 2022-05-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220520_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='element_2',
            field=models.IntegerField(blank=True, choices=[(1, 'ディーディーコング'), (2, 'シュルク')], null=True, verbose_name='キャラ1'),
        ),
    ]