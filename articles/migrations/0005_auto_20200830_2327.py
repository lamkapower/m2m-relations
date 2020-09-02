# Generated by Django 2.2.10 on 2020-08-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200830_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(to='articles.Article'),
        ),
    ]