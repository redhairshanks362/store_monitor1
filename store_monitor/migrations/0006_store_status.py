# Generated by Django 4.2.5 on 2023-09-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_monitor', '0005_delete_store_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='store_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('timestamp_utc', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
