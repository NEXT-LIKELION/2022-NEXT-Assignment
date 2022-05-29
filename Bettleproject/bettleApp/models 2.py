from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

class Team(models.Model):
    hostUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hostUser', max_length=50)
    firstMember = models.CharField(max_length=200)
    secondMember = models.CharField(max_length=200)
    thirdMember = models.CharField(max_length=200)
    fourthMember = models.CharField(max_length=200)
    Tier = models.CharField(max_length=100)
    bulletBet = models.IntegerField(default=0)
    matchDates = models.CharField(max_length=500, null=True)

    def set_matchDates(self, date):
        self.matchDates = json.dumps(date)
        self.save()

    def get_matchDates(self):
        return json.loads(self.matchDates)



