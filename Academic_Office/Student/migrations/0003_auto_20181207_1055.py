# Generated by Django 2.1.2 on 2018-12-07 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_remove_courses_c_assignments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_marks', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='A_marks',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='A_weightage',
        ),
        migrations.AddField(
            model_name='assignment',
            name='A_course',
            field=models.ForeignKey(default='001', on_delete=django.db.models.deletion.CASCADE, to='Student.Courses'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='A_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='A_max_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='assign_marks',
            name='A_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Assignment'),
        ),
        migrations.AddField(
            model_name='assign_marks',
            name='A_sid',
            field=models.ForeignKey(default='2017010108', on_delete=django.db.models.deletion.CASCADE, to='Student.Students'),
        ),
    ]
