# Generated by Django 4.0.3 on 2022-04-09 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0044_delete_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='page_acces',
            name='admin',
            field=models.OneToOneField(limit_choices_to={'is_superuser': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page_acces',
            name='user',
            field=models.OneToOneField(limit_choices_to={'is_superuser': False}, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
