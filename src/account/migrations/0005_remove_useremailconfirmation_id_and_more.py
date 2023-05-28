# Generated by Django 4.1.4 on 2023-01-29 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_useremailconfirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useremailconfirmation',
            name='id',
        ),
        migrations.AddField(
            model_name='useremailconfirmation',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useremailconfirmation',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='Confirmation token'),
        ),
    ]
