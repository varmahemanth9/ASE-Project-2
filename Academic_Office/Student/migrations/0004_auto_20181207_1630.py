# Generated by Django 2.1.2 on 2018-12-07 11:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20181207_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradingPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('G_weightage', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.AlterField(
            model_name='assign_marks',
            name='A_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='A_max_marks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gradingpolicy',
            name='G_assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Assignment'),
        ),
    ]
