# Generated by Django 3.1.7 on 2021-06-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0005_auto_20210608_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='table',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]