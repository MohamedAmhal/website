# Generated by Django 4.2 on 2024-02-12 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_cartorder_oid_cartorder_shipping_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]