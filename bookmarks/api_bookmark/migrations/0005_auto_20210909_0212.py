# Generated by Django 3.2.7 on 2021-09-09 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookmark', '0004_alter_bookmark_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
