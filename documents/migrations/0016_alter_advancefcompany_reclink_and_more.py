# Generated by Django 4.0.3 on 2022-04-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0015_delete_newfcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancefcompany',
            name='RecLink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='receiDepPay',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]