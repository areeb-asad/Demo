# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    content = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)