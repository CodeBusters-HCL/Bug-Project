# Generated by Django 3.1.1 on 2020-10-08 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0023_auto_20201007_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='issue_id',
            new_name='issueid',
        ),
    ]