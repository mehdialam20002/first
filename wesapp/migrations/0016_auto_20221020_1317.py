# Generated by Django 3.1 on 2022-10-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0015_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
