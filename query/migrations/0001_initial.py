# Generated by Django 3.1.5 on 2021-01-28 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='querydata',
            fields=[
                ('querydata_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('query', models.CharField(max_length=300)),
                ('contacted_via', models.CharField(max_length=50)),
                ('follow_up', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customerdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='query.querydata')),
            ],
        ),
    ]