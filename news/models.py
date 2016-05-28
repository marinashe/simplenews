from django.db import models

# Create your models here.
class News(models.Model):

    posted_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=200)
