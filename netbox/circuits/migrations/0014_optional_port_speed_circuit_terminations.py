# Generated by Django 2.0.9 on 2018-11-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuits', '0013_merge_20181012_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuittermination',
            name='port_speed',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Port speed (Kbps)'),
        ),
    ]