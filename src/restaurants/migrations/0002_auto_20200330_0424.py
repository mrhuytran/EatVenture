# Generated by Django 3.0.2 on 2020-03-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestsellingitem',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_name',
            field=models.CharField(max_length=100),
        ),
    ]