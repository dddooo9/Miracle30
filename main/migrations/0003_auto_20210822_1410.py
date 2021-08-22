# Generated by Django 3.2.5 on 2021-08-22 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_goal_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='deadline',
            field=models.DateField(default=datetime.date(2021, 8, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='member_limit',
            field=models.IntegerField(default=10),
        ),
    ]
