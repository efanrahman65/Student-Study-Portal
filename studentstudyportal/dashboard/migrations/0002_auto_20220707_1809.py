# Generated by Django 3.2.14 on 2022-07-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='description',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
