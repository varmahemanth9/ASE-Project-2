# Generated by Django 2.1.3 on 2018-11-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0011_auto_20181127_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='C_books',
        ),
        migrations.AddField(
            model_name='book',
            name='B_cid',
            field=models.ForeignKey(default='000', on_delete=django.db.models.deletion.CASCADE, to='Student.Courses'),
            preserve_default=False,
        ),
    ]
