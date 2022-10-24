import datetime
from random import choices

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('polls:home', args=[self.name])


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Data(models.Model):
    specific_id = models.CharField('specific_id', max_length=156)
    horizon_width = models.CharField('horizon_width', max_length=100)
    vertical_width = models.CharField('vertical_width', max_length=100)
    x_location = models.CharField('x_location', max_length=100)
    y_location = models.CharField('y_location', max_length=100)
    def __str__(self):
        return str(self.specific_id)

class KospiPredict(models.Model):
    date = models.DateField("날짜", max_length=10, null=False, unique=True)
    close = models.FloatField("종가", null=True)
    open = models.FloatField("시가", null=True)
    # cate = (('aa','bb'),('dd','ee'))
    # catt = models.CharField(max_length = 10, choices = cate)

# Create your models here.


class TPC_H_QUERY(models.Model):
    query_id = models.IntegerField('queryid')
    work_id = models.IntegerField('workid')
    full_query = models.CharField('full_query', max_length=600)
    summary_work = models.CharField('summary_work', max_length=200)
    def __str__(self):
        return str(self.query_id)



class Side_Var(models.Model):
    seqnum = models.IntegerField('seqnum')
    name = models.CharField('fullname', max_length=100)
    def __str__(self):
        return str(self.seqnum)