# Generated by Django 2.0.9 on 2018-10-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0064_merge_20181012_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True),
        ),
    ]
