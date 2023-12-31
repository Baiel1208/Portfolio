# Generated by Django 4.2.7 on 2023-11-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=255, verbose_name='Когда учился')),
                ('title', models.CharField(max_length=255, verbose_name='Где учился')),
                ('descriptions', models.TextField(verbose_name='Что учил')),
            ],
            options={
                'verbose_name': 'ОБРАЗОВАНИЕ',
                'verbose_name_plural': 'ОБРАЗОВАНИЯ',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=255, verbose_name='Время работы')),
                ('title', models.CharField(max_length=255, verbose_name='Где работал')),
                ('descriptions', models.TextField(verbose_name='Что делал')),
            ],
            options={
                'verbose_name': 'Опыт',
                'verbose_name_plural': 'Опыты',
            },
        ),
    ]
