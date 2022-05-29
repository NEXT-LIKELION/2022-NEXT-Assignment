from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.

#user의 닉네임 정보


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=30)
    account = models.TextField()

    def __str__(self):
        return self.nickname


class Participation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "participation_set")
    time_late = models.IntegerField()

    def __str__(self):
        return self.profile.nickname


#돼지 생성 정보
class Pig(models.Model):
    pig_name = models.CharField(max_length=20)
    pig_description = models.TextField()
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='host_set')
    participants = models.ManyToManyField(Participation, related_name="pig", blank=True)
    exchange_rate = models.FloatField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.pig_name

  
class Schedule(models.Model):
    pig_info = models.ForeignKey('Pig', on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=20)
    schedule_description = models.TextField()
    where_to_meet = models.TextField()
    when_to_meet = models.DateTimeField()
    arrived = models.ManyToManyField(Profile, related_name='arrived_set', blank=True)

    def __str__(self):
        return self.schedule_name


