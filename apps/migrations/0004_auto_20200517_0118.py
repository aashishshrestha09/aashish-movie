# Generated by Django 3.0.6 on 2020-05-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20200517_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
