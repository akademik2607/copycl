# Generated by Django 5.0.3 on 2024-04-20 12:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Номер заказа'),
        ),
    ]
