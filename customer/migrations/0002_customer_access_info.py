# Generated by Django 3.2.9 on 2021-11-21 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_access_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nsu_ID', models.BooleanField(default=False)),
                ('first_name', models.BooleanField(default=False)),
                ('last_name', models.BooleanField(default=False)),
                ('department', models.BooleanField(default=False)),
                ('program', models.BooleanField(default=False)),
                ('batch', models.BooleanField(default=False)),
                ('email', models.BooleanField(default=False)),
                ('photo', models.BooleanField(default=False)),
                ('father_name', models.BooleanField(default=False)),
                ('mother_name', models.BooleanField(default=False)),
                ('gender', models.BooleanField(default=False)),
                ('data_of_birth', models.BooleanField(default=False)),
                ('address', models.BooleanField(default=False)),
                ('religion', models.BooleanField(default=False)),
                ('citizenship', models.BooleanField(default=False)),
                ('marital_status', models.BooleanField(default=False)),
                ('blood_group', models.BooleanField(default=False)),
                ('covid19_vax_status', models.BooleanField(default=False)),
                ('contact_number', models.BooleanField(default=False)),
                ('annual_income', models.BooleanField(default=False)),
                ('earning_source', models.BooleanField(default=False)),
                ('annual_expenditure', models.BooleanField(default=False)),
                ('academic_info', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer_info')),
            ],
        ),
    ]