from django.db import models
from django.utils import timezone

# Create your models here.

class CPnumber(models.Model):
    qihao = models.IntegerField(primary_key=True)
    shuzi = models.CharField(max_length=7)
    wan = models.IntegerField(default=-1)
    qian = models.IntegerField(default=-1)
    bai = models.IntegerField(default=-1)
    shi = models.IntegerField(default=-1)
    ge = models.IntegerField(default=-1)
    created_time = models.DateTimeField(default=timezone.now())
    
    def __unicode__(self):
        return self.shuzi

class CPUrl(models.Model):
    ip = models.CharField(max_length=16)
    url = models.CharField(max_length=300)
    used = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url
