# Generated by Django 2.2.13 on 2021-01-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_auto_20181031_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]