# Generated by Django 4.0.6 on 2022-07-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(db_column='student_name', max_length=255)),
                ('department_name', models.CharField(db_column='department_name', max_length=255)),
                ('created_on', models.DateField(db_column='created_on')),
                ('updated_on', models.DateField(auto_now=True, db_column='updated_on')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(db_column='subject', max_length=255)),
                ('marks', models.CharField(db_column='marks', max_length=255)),
                ('created_on', models.DateField(db_column='created_on')),
                ('updated_on', models.DateField(auto_now=True, db_column='updated_on')),
                ('student_name', models.ForeignKey(db_column='student_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.student')),
            ],
        ),
    ]
