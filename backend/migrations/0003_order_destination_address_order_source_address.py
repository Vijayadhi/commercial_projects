# Generated by Django 5.1.7 on 2025-03-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_product_order_cart_transaction_transport'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='destination_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='source_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
