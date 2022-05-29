from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)


class Test(models.Model):
    # category = models.CharField(max_length=50, blank=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tests')

    testname = models.TextField()

    truetag1 = models.CharField(max_length=30, null=True)
    truetag2 = models.CharField(max_length=30, null=True)
    truetag3 = models.CharField(max_length=30, null=True)
    truetag4 = models.CharField(max_length=30, null=True)
    truetag5 = models.CharField(max_length=30, null=True)

    falsetag1 = models.CharField(max_length=30, null=True)
    falsetag2 = models.CharField(max_length=30, null=True)
    falsetag3 = models.CharField(max_length=30, null=True)
    falsetag4 = models.CharField(max_length=30, null=True)
    falsetag5 = models.CharField(max_length=30, null=True)


# class UserTest(models.Model):
class Guest(models.Model):
    name = models.CharField(max_length=20)
