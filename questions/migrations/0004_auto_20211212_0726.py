# Generated by Django 2.2 on 2021-12-12 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20211209_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]