# Generated by Django 3.1.5 on 2021-01-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_auto_20210129_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querydata',
            name='query',
            field=models.CharField(max_length=300),
        ),
    ]
