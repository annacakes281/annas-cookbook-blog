# Generated by Django 3.2.21 on 2023-10-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_site', '0006_alter_tip_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
    ]
