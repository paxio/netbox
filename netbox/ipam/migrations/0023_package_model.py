# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0022_merge_20180222_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'Loopback'), (15, 'Static route'), (20, 'Secondary'), (30, 'Anycast'), (40, 'VIP'), (41, 'VRRP'), (42, 'HSRP'), (43, 'GLBP'), (44, 'CARP')], help_text='The functional role of this IP', null=True, verbose_name='Role'),
        ),
    ]
