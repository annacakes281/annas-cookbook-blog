# Generated by Django 3.2.21 on 2023-10-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_site', '0013_auto_20231019_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='category',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Drinks'), (2, 'Sauces')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Drinks'), (2, 'Sauces')], default=0),
        ),
    ]
