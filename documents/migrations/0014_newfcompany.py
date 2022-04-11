# Generated by Django 4.0.3 on 2022-04-10 19:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0046_alter_page_acces_admin'),
        ('documents', '0013_alter_advancefcompany_reclink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='newFCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('depostieAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('paymenetAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('DepPAyDate', models.DateField()),
                ('netAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('FCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.f_company')),
            ],
        ),
    ]
