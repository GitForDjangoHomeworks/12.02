# Generated by Django 4.1.5 on 2023-01-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_class_day'),
        ('teachers', '0009_alter_teacher_birth_day'),
        ('classes', '0009_alter_classbyday_options_remove_classbyday_week_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50, verbose_name='Занятие')),
                ('student', models.ManyToManyField(to='students.student', verbose_name='Студет')),
                ('teacher', models.ManyToManyField(to='teachers.teacher', verbose_name='Преподаватель')),
            ],
        ),
        migrations.DeleteModel(
            name='ClassWithTeacher',
        ),
    ]
