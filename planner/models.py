from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.TextField()


    def __str__(self):
        
        return self.author
# Create your models here.


class EidEvent(models.Model):
    title  = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title