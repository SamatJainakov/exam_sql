# Generated by Django 4.2 on 2023-04-11 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('date_started', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('month_to_learn', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('work_study_place', models.CharField(blank=True, max_length=20, null=True)),
                ('has_own_notebook', models.BooleanField()),
                ('preferred_os', models.CharField(choices=[('windows', 'Windows'), ('mac', 'MacOS'), ('linux', 'Linux')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('main_work', models.CharField(blank=True, max_length=20, null=True)),
                ('experience', models.DateField()),
                ('student', models.ManyToManyField(through='user.Course', to='user.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]
