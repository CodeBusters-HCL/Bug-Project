# Generated by Django 3.1.1 on 2020-10-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0022_auto_20201007_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='enops',
        ),
        migrations.AddField(
            model_name='issue',
            name='project_type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]