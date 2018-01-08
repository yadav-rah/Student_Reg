from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    usn = models.CharField(max_length=10,unique=True,primary_key=True)
    college = models.CharField(max_length=6,default='NA')

    def __str__(self):
        return self.usn

class StudMarks(models.Model):
    usn = models.CharField(primary_key=True,max_length=10,unique=True)
    sem_1 = models.FloatField(blank=True,default=0)
    sem_2 = models.FloatField(blank=True,default=0)
    sem_3 = models.FloatField(blank=True,default=0)
    sem_4 = models.FloatField(blank=True,default=0)
    sem_5 = models.FloatField(blank=True,default=0)
    sem_6 = models.FloatField(blank=True,default=0)
    sem_7 = models.FloatField(blank=True,default=0)
    sem_8 = models.FloatField(blank=True,default=0)
