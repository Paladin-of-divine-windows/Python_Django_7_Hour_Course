# Generated by Django 4.0.3 on 2022-04-10 13:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_rename_massage_message_alter_room_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=b'I01\n', related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
