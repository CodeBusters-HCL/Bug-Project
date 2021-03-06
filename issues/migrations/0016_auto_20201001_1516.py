# Generated by Django 3.1.1 on 2020-10-01 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0015_auto_20201001_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_to_username',
            field=models.ForeignKey(default='Not assigned to anyone yet', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
