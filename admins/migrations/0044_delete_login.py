# Generated by Django 4.0.3 on 2022-04-09 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0043_alter_login_last_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]