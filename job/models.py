from __future__ import unicode_literals

from django.db import models

from django.contrib.postgres.fields import ArrayField


class jobinfo(models.Model):
    title=models.CharField(max_length=40)
    companyname=models.CharField(max_length=50)

class skillset(models.Model):
    job=models.ForeignKey(jobinfo)
    skill=models.CharField(max_length=40)
    experience=models.IntegerField(default=0)

# Create your models here.
