# Generated by Django 2.2 on 2021-12-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20211118_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]