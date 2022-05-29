from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone



class Category_Item(models.Model):
    item = models.CharField(max_length=255, null=True, default='')
    def __str__(self):
        return self.item


class Email_period(models.Model):
    period = models.CharField(max_length=15, null=True) 
    
    def __str__(self):
        return self.period
class User(AbstractUser):
    #unique=True 유일한 값으로 변경해주기
    #null=True빈값 입력가능하도록 하기
    department = models.CharField(max_length=30, null=True, default='')
    nickname = models.CharField(max_length=15, null=True, default='', error_messages={'unique': '이미 사용중인 닉네임입니다.'}) 
    #nickname = models.CharField(max_length=15, unique=True, null=True, default='', error_messages={'unique': '이미 사용중인 닉네임입니다.}) 
    
    phone_number = PhoneNumberField(null=True)
    

    #category를 폴린키로 가져올 수도 있을 것 같은디--> 계속 유저가 생성할 수 있게, 참조할 수 있게, 1대 다로 참조할 수 있게 구성
    category = models.ForeignKey(Category_Item, models.CASCADE, related_name="user_categorys", null=True, default='')
    email_period = models.ForeignKey(Email_period, models.CASCADE, related_name="user_emails", null=True, default='')
    # email_period = models.CharField(max_length=15, null=True, default="7") 
    is_active = models.BooleanField(default=True)
    is_premier = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse("index")
    
#이렇게 하면 호출했을 때, 이메일로 호출하도록 만듬.
#allauth는 기본 유저 정보를 입력하고, 다음 닉네임같은 값들을 넣어준다.


    
    # def get_absolute_url(self):
    #     return reverse("index")

class Notice_content(models.Model):
    title = models.CharField(max_length=200, null=True, default='')
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=200, null=True, default='')
    link = models.TextField(null=True)
    category = models.ForeignKey(Category_Item, models.CASCADE, related_name="notice_categorys", null=True, default='')
    content = models.ForeignKey(Notice_content, models.CASCADE, related_name="notice_contents", null=True, default='')
    post_date = models.DateField()
    end_date = models.DateField(default=timezone.now)
    source = models.CharField(max_length=255,null=True, default='')

    def __str__(self):
        return self.title


