# Generated by Django 2.1.2 on 2018-12-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_id', models.CharField(max_length=15)),
                ('T_name', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('T_email', models.EmailField(blank=True, default='farazuddin.m17@iiits.in', max_length=254)),
                ('T_password', models.CharField(max_length=50)),
                ('T_course_id', models.ForeignKey(on_delete=None, to='Student.Courses')),
            ],
        ),
    ]
