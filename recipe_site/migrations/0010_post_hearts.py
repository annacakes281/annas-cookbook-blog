# Generated by Django 3.2.21 on 2023-10-12 10:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe_site', '0009_delete_contactme'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hearts',
            field=models.ManyToManyField(blank=True, related_name='recipe_hearts', to=settings.AUTH_USER_MODEL),
        ),
    ]
