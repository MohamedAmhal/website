# Generated by Django 4.2 on 2024-02-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_cartorder_email_cartorder_full_name_cartorder_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='stripe_payment_intent',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
