# Generated by Django 4.0.3 on 2022-03-21 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0014_alter_login_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 21, 22, 29, 4, 725489)),
        ),
    ]
