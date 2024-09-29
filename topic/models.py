from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class StudentUser(AbstractUser):
    group = models.CharField('group', max_length=8, null=True, blank=True)
    degree = models.CharField('degree', max_length=1, null=True, blank=True)
    surname = models.CharField('surname', max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Profile(models.Model):
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='student_user', null=True)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return str(self.age)

    class Meta:
        verbose_name = "Shaxsiy kabinet"
        verbose_name_plural = "Shaxsiy kabinetlar"


class PhotoModel(models.Model):
    lesson_number = models.CharField(max_length=20)
    description_photo = models.ImageField()

    def __str__(self):
        return str(self.lesson_number)

    class Meta:
        verbose_name = "Dars rasmi"
        verbose_name_plural = "Dars rasmlari"


class Lesson(models.Model):
    number = models.CharField('Number', max_length=20)
    title = models.CharField('Theme', max_length=200)
    description = RichTextUploadingField()
    description_photo = models.ManyToManyField(PhotoModel)
    practice = RichTextField()
    photo = models.ImageField()
    order = models.IntegerField()
    video = models.FileField('Video', upload_to='videos/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"


class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


class AboutProject(models.Model):
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    text = RichTextUploadingField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Loyiha haqida"


class UsefulLink(models.Model):
    icon = models.ImageField(upload_to='media/images', null=True, blank=True)
    title = models.CharField(max_length=250)
    link = models.URLField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Foydali link'
        verbose_name_plural = 'Foydali linklar'

    def __str__(self):
        return self.title


class ControlWork(models.Model):
    class WorkType(models.TextChoices):
        JN = 'jn', 'Joriy Nazorat'
        ON = 'on', 'Oraliq Nazorat'
        YN = 'yn', 'Yakuniy Nazorat'

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    type = models.CharField(max_length=20, choices=WorkType.choices, default=WorkType.JN)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Nazorat ishi'
        verbose_name_plural = 'Nazorat ishlari'


class Glossary(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/images', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Glossariy'
        verbose_name_plural = 'Glossariy'



class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField('Email', max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'