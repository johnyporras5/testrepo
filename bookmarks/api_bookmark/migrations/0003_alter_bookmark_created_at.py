# Generated by Django 3.2.7 on 2021-09-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookmark', '0002_auto_20210908_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]
