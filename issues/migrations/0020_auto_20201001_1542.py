# Generated by Django 3.1.1 on 2020-10-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0019_auto_20201001_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_to_email',
            field=models.EmailField(default='Not assigned  yet', max_length=254),
        ),
    ]
