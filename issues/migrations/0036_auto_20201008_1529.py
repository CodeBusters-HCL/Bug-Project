# Generated by Django 3.1.1 on 2020-10-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0035_auto_20201008_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_file',
            field=models.FileField(blank=True, upload_to='issue_file/%Y/%m/%d/'),
        ),
    ]
