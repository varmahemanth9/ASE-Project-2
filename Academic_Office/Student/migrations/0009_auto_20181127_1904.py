# Generated by Django 2.1.3 on 2018-11-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_auto_20181127_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='S_courses',
            new_name='C_books',
        ),
    ]