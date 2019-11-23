from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Starring(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    nationality = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='titles')
    starring = models.ForeignKey(Starring, on_delete=models.CASCADE, related_name='starrings')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Rate(models.Model):
    note = models.IntegerField()
    title = models.ForeignKey(Title, related_name='titles', on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ratings = models.ManyToManyField(Rate, related_name='ratings')

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name