# Generated by Django 5.0.4 on 2024-04-14 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(help_text='leave start date is on...', null=True, verbose_name='start Date')),
                ('enddate', models.DateField(help_text='coming back on ...', null=True, verbose_name='End Date')),
                ('leavetype', models.CharField(choices=[('sick', 'Sick leave'), ('emargancy', 'Emergancy leave'), ('martenity', 'Martenity leave'), ('study', 'Study leave')], default='sick', max_length=25, null=True)),
                ('reason', models.CharField(blank=True, help_text='add additional information for leave', max_length=255, null=True, verbose_name='Reason for Leave')),
                ('defaultdays', models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='Leave days per year counter')),
                ('status', models.CharField(default='pending', max_length=12)),
                ('is_approved', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'ordering': ['-created'],
            },
        ),
    ]
