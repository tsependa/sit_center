# Generated by Django 2.2.2 on 2019-07-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='priority',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='cover',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
