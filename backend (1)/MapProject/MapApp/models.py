from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    information = models.TextField(null=True)

    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Info(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    entrance = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.title

class Lounge(models.Model):
    schools = models.ForeignKey(School, related_name="lounge", on_delete=models.CASCADE)
    category = models.CharField(max_length=10, null=True)
    lounge = models.CharField(max_length=50)
    lounge_info = models.TextField(null=True)
    photos = models.ImageField()

    def __str__(self):
        return self.lounge    

class Door(models.Model):
    building = models.ForeignKey(School, on_delete=models.CASCADE)
    names = models.ForeignKey(Info, on_delete=models.CASCADE)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
