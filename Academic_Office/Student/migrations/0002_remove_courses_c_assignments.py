# Generated by Django 2.1.2 on 2018-12-07 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='C_assignments',
        ),
    ]