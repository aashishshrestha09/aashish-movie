# Generated by Django 3.0.6 on 2020-05-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.URLField(default='https://joyfulharmony.org/wp16/wp-content/uploads/2018/03/No-Movies-For-Two-Years.jpg'),
        ),
    ]
