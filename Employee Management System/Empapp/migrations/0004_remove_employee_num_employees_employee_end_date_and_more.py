# Generated by Django 4.2.9 on 2024-01-21 11:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Empapp', '0003_department_basic_pay_employee_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='num_employees',
        ),
        migrations.AddField(
            model_name='employee',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.PositiveIntegerField(default=36),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='date_range',
            field=models.CharField(choices=[('start_date', 'Start Date'), ('end_date', 'End Date')], max_length=10),
        ),
    ]