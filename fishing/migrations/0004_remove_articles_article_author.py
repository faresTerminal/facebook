# Generated by Django 2.1.7 on 2020-08-02 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishing', '0003_auto_20200802_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='article_author',
        ),
    ]