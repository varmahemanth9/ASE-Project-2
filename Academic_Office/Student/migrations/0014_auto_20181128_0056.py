# Generated by Django 2.1.3 on 2018-11-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0013_auto_20181128_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Book_id',
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]