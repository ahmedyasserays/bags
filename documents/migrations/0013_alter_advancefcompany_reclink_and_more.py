# Generated by Django 4.0.3 on 2022-04-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0012_alter_advancefcompany_fcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancefcompany',
            name='RecLink',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='newFCompany',
        ),
    ]