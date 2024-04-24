# Generated by Django 5.0.4 on 2024-04-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_alter_leaverequest_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='enddate',
            field=models.DateField(help_text='coming back on ...', null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='startdate',
            field=models.DateField(help_text='leave start date is on ..', null=True, verbose_name='Start Date'),
        ),
    ]
