# Generated by Django 5.0.4 on 2024-04-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_employee_total_leave_balance_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='', upload_to='static/build/images/'),
        ),
    ]
