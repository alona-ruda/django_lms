# Generated by Django 4.1.1 on 2022-10-23 19:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import groups.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.datetime.utcnow, validators=[groups.validators.validate_start_date])),
                ('end_date', models.DateField(blank=True, null=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.course')),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
