# Generated by Django 4.2.7 on 2023-11-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('age', models.CharField(max_length=3, verbose_name='Возраст')),
                ('nation', models.CharField(max_length=255, verbose_name='Нация')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('telegram', models.CharField(max_length=255, verbose_name='Username телеграм')),
                ('language', models.CharField(max_length=255, verbose_name='Знание языка')),
                ('year', models.CharField(max_length=255, verbose_name='Годы опыта')),
                ('projects', models.CharField(max_length=255, verbose_name='Завершенные проекты')),
                ('clients', models.CharField(max_length=255, verbose_name='Счастливые клиенты')),
                ('awards', models.CharField(max_length=255, verbose_name='Полученные награды')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_user/', verbose_name='Загрузите фотографию')),
                ('name', models.CharField(max_length=100, verbose_name='Введите ФИО')),
                ('work', models.CharField(max_length=50, verbose_name='Вввдите профессию')),
                ('descriptions', models.TextField(verbose_name='Введите биографию')),
            ],
            options={
                'verbose_name': 'Информация пользователя',
                'verbose_name_plural': 'Информации пользователей',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=255, verbose_name='Навыки')),
                ('ownership', models.IntegerField(verbose_name='На сколько процент владеешь')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
