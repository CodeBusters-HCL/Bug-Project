# Generated by Django 3.1.1 on 2020-10-01 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0016_auto_20201001_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_to_username',
            field=models.ForeignKey(default='not_assigned_to_@_anyone_yet_.com', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
