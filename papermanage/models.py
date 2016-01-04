from django.db import models

# Create your models here.
class Paper(models.Model):
    PaperID=models.CharField(max_length=100,primary_key=True)
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Keyword=models.CharField(max_length=100)
    Publisher=models.CharField(max_length=100)
    PublishDate=models.DateField()
    Grade1=models.CharField(max_length=100)
    Grade2=models.CharField(max_length=100)
    Grade3=models.CharField(max_length=100)
    Summary=models.CharField(max_length=2000)
    File=models.FileField(upload_to='./static/load')
    address=models.CharField(max_length=500)
    
    
    def __unicode(self):
        return self.Title
    
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=50)


    def __unicode__(self):
        return self.username

class Pbpaper(models.Model):
    PaperID=models.CharField(max_length=100,primary_key=True)
    Title=models.CharField(max_length=100)
    Author1=models.CharField(max_length=100)
    Author2=models.CharField(max_length=100)
    Author3=models.CharField(max_length=100)
    Author4=models.CharField(max_length=100)
    Keyword=models.CharField(max_length=100)
    Publisher=models.CharField(max_length=100)
    PublishDate=models.DateField()
    Grade1=models.CharField(max_length=100)
    Grade2=models.CharField(max_length=100)
    Grade3=models.CharField(max_length=100)
    Summary=models.CharField(max_length=2000)
    Score=models.IntegerField()
    File=models.FileField(upload_to='./static/load')
    address=models.CharField(max_length=500)
    
