# Generated by Django 4.1.1 on 2022-10-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, related_name='groups', to='teachers.teacher'),
        ),
    ]
