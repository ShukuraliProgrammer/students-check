from distutils.command.upload import upload
from distutils.text_file import TextFile
from pyexpat import model
from re import T
from tokenize import group
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class StudentUser(AbstractUser):
    gruh = models.CharField('Gruh', max_length=8, null=True, blank=True)
    kursi = models.CharField('Kursi', max_length=1, null=True, blank=True)
    sharifi = models.CharField('Sharifi', max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='student_user', null=True)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return str(self.age)


class Lesson(models.Model):
    title = models.CharField('Mavzusi', max_length=200)
    description = models.TextField()
    photo = models.ImageField()
    # test = models.ForeignKey(Quiz, related_name='test')

    video = models.FileField('Video lavha', upload_to='videos/', null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


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
