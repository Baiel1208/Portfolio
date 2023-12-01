from django.db import models

# Create your models here.
class InfoUser(models.Model):
    image = models.ImageField(
        upload_to="image_user/",
        verbose_name="Загрузите фотографию"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Введите ФИО"
    )
    work = models.CharField(
        max_length=50,
        verbose_name="Вввдите профессию"
    )
    descriptions = models.TextField(
        verbose_name="Введите биографию"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Информация пользователя"
        verbose_name_plural = "Информации пользователей"


class About(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия"
    )
    age = models.CharField(
        max_length=3,
        verbose_name="Возраст"
    )
    nation = models.CharField(
        max_length=255,
        verbose_name="Нация"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    telegram = models.CharField(
        max_length=255,
        verbose_name="Username телеграм"
    )
    language = models.CharField(
        max_length=255,
        verbose_name="Знание языка"
    )
    year = models.CharField(
        max_length=255,
        verbose_name="Годы опыта"
    )
    projects = models.CharField(
        max_length=255,
        verbose_name='Завершенные проекты'
    )
    clients = models.CharField(
        max_length=255,
        verbose_name="Счастливые клиенты"
    )
    awards = models.CharField(
        max_length=255,
        verbose_name="Полученные награды"
    )
    title_contact = models.CharField(
        max_length=255,
        verbose_name='Заголовок для контактов'
    )
    descriptions_contact = models.CharField(
        max_length=255,
        verbose_name='Описание для контактов'
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name="Twitter",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="Youtube",
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.first_name}  -  {self.last_name}'


    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"


class Skills(models.Model):
    skills = models.CharField(
        max_length=255,
        verbose_name='Навыки'
    )
    ownership = models.IntegerField(
        verbose_name='На сколько процент владеешь'
    )


    def __str__(self):
        return f'{self.skills}  -  {self.ownership}'


    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class Experience(models.Model):
    years = models.CharField(
        max_length=255,
        verbose_name='Время работы'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Где работал'
    )
    descriptions = models.TextField(
        verbose_name='Что делал'
    )


    def __str__(self):
        return f'{self.title}  -  {self.years}'


    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыты"


class Education(models.Model):
    years = models.CharField(
        max_length=255,
        verbose_name='Когда учился'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Где учился'
    )
    descriptions = models.TextField(
        verbose_name='Что учил'
    )


    def __str__(self):
        return f'{self.title}  -  {self.years}'


    class Meta:
        verbose_name = "ОБРАЗОВАНИЕ"
        verbose_name_plural = "ОБРАЗОВАНИЯ"


class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )


    def __str__(self) -> str:
        return f'{self.name} -- {self.email}'
    

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Portfolio(models.Model):
    project = models.CharField(
        max_length=255,
        verbose_name='Название проекта'
    )
    languages = models.CharField(
        max_length=200,
        verbose_name='Языки програмирование'
    )
    client = models.CharField(
        max_length=255,
        verbose_name='Клиент'
    )
    link = models.CharField(
        max_length=255,
        verbose_name='Ссылка на проект'
    )
    image = models.ImageField(
        upload_to='portfolio_image/',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return f'{self.project}'
    

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Blog(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    direction = models.CharField(
        max_length=200,
        verbose_name='Направление'
    )
    title  =  models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    image = models.ImageField(
        upload_to='blog_image/',
        verbose_name='Картина'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )


    def __str__(self) -> str:
        return f'{self.name}'
    

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'