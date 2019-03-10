from django.db import models

# Create your models here.
class Ask(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    
   

    def __str__(self):
        return self.name

class Ans(models.Model):
    user = models.CharField(max_length=150)
    survey = models.CharField(max_length = 150)
    done = models.BooleanField()
    rate = models.CharField(max_length = 1)
   
   

    def __str__(self):
        return self.name

