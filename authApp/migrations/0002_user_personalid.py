# Generated by Django 3.2.8 on 2021-10-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='personalID',
            field=models.CharField(default=123, max_length=30, verbose_name='PersonalID'),
            preserve_default=False,
        ),
    ]
