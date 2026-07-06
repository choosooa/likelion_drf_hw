from django.db import models

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    debut = models.DateField()
    
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    release = models.DateField()
    content = models.TextField()
    