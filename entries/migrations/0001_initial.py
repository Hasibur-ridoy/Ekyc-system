# Generated by Django 3.2.9 on 2021-11-20 13:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('couse_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('course_title', models.CharField(blank=True, max_length=100, null=True)),
                ('course_desc', models.TextField(blank=True, max_length=100, null=True)),
                ('course_credit', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nsu_id', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=5)),
                ('program', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('photo', models.ImageField(default='photos/profile-picture-default.png', upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_info',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='entries.student_info')),
                ('annual_income', models.IntegerField(blank=True, null=True)),
                ('earning_source', models.CharField(blank=True, max_length=100, null=True)),
                ('annual_expenditure', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hsc_equivlent',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='entries.student_info')),
                ('college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.IntegerField(blank=True, null=True)),
                ('passing_year', models.IntegerField(blank=True, null=True)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('medium', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='entries.student_info')),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=10, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=10, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=20, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=20, null=True)),
                ('covid19_vax_status', models.CharField(blank=True, choices=[('Vaccinated', 'Vaccinated'), ('Unvaccinated', 'Unvaccinated')], max_length=20, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ssc_equivlent',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='entries.student_info')),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.IntegerField(blank=True, null=True)),
                ('passing_year', models.IntegerField(blank=True, null=True)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('medium', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('ga_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(blank=True, choices=[('FALL', 'FALL'), ('SUMMER', 'SUMMER'), ('SPRING', 'SPRING')], max_length=20, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('F', 'F'), ('I', 'I'), ('W', 'W')], max_length=10, null=True)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.course')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.student_info')),
            ],
        ),
    ]
