# Generated by Django 4.1.4 on 2023-01-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_card_created_by_card_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_global',
            field=models.BooleanField(default=False, verbose_name='Is this card global'),
        ),
    ]
