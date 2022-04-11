# Generated by Django 4.0.3 on 2022-04-09 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0046_alter_page_acces_admin'),
        ('documents', '0010_alter_newfcompany_fcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uplaodingdocument',
            name='DocumentType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.new_document'),
        ),
        migrations.AlterField(
            model_name='uplaodingdocument',
            name='itemType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.new_item'),
        ),
    ]