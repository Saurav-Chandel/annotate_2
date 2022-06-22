import datetime
import django
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)     #return true if question in published the cuurent day and the furture days.
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now     #returns true if the question is published only in the current day.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choice')
    choice_text = models.CharField(max_length=200,null=True,blank=True)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        # return "Choice: {}, Question:{}".format(self.choice_text, self.question.question_text)
        return self.choice_text


class City(models.Model):
    # ...
    name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    # ...
    p_name=models.CharField(max_length=100,null=True,blank=True)
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.p_name)

class Book(models.Model):
    # ...
    b_name=models.CharField(max_length=100,null=True,blank=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.b_name)

from django.conf import settings

#filesystemStorages
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Car(models.Model):
    
    photo = models.ImageField(storage=fs)