from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Starring(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    nationality = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='titles')
    starring = models.ForeignKey(Starring, on_delete=models.CASCADE, related_name='starrings')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Rate(models.Model):
    note = models.IntegerField()
    title = models.ForeignKey(Title, related_name='titles', on_delete=models.CASCADE)
    review = models.TextField(max_length=3000, null=True)
    profile = models.ForeignKey(Profile, related_name='ratings', on_delete=models.CASCADE)