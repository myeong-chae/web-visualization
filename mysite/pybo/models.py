from statistics import mode
from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Query(models.Model):
    Query_ID = models.IntegerField()
    Full_Query = models.CharField(max_length=600)

class Work(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    Work_ID = models.IntegerField()
    Summary_Work = models.CharField(max_length=100)

class Metric(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    CSD_CPU = models.FloatField()
    SE_CPU = models.FloatField()
    DBC_CPU = models.FloatField()
    CSD_Memory = models.FloatField()
    SE_Memory = models.FloatField()
    DBC_Memory = models.FloatField()
    CSD_Power = models.FloatField()
    SE_Power = models.FloatField()
    DBC_Power = models.FloatField()
    CSD_Network = models.FloatField()
    SE_Network = models.FloatField()
    DBC_Network = models.FloatField()
    CSD_IO = models.FloatField()
    SE_IO = models.FloatField()
    DBC_IO = models.FloatField()
    CSD_Time = models.FloatField()
    SE_Time = models.FloatField()
    DBC_Time = models.FloatField()

class KospiPredict(models.Model):
    date = models.DateField("날짜", max_length=10, null=False, unique=True)
    close = models.FloatField("종가", null=True)
    open = models.FloatField("시가", null=True)
    # cate = (('aa','bb'),('dd','ee'))


