from django.db import models

# Create your models here.
class QRinfo(models.Model):
    url = models.TextField() 
    img_path = models.CharField(max_length=4096) #max_path_length
    info = models.TextField()

