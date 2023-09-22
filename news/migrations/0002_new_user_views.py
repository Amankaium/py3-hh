# Generated by Django 4.2.2 on 2023-08-07 07:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='user_views',
            field=models.ManyToManyField(blank=True, related_name='new_views', to=settings.AUTH_USER_MODEL),
        ),
    ]