# Generated by Django 2.1.3 on 2018-11-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_auto_20181118_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='S_courses',
            field=models.ManyToManyField(to='Student.Book'),
        ),
    ]
