# Generated by Django 5.0.3 on 2024-05-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='personalMarketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
