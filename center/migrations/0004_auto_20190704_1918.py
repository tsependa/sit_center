# Generated by Django 2.2.2 on 2019-07-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0003_auto_20190704_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='url',
        ),
        migrations.AddField(
            model_name='report',
            name='sql',
            field=models.TextField(blank=True),
        ),
    ]
