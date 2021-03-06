# Generated by Django 3.0.5 on 2020-06-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mcq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queustion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.BooleanField(default=False)),
                ('option1', models.CharField(max_length=50)),
                ('op2', models.BooleanField(default=False)),
                ('option2', models.CharField(max_length=50)),
                ('op3', models.BooleanField(default=False)),
                ('option3', models.CharField(max_length=50)),
                ('op4', models.BooleanField(default=False)),
                ('option4', models.CharField(max_length=50)),
                ('next', models.IntegerField()),
            ],
        ),
    ]
