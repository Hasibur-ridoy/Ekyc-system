# Generated by Django 3.2.9 on 2021-11-21 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_access_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_access_info',
            name='customer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer_info'),
        ),
    ]
