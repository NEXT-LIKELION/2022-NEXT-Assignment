from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import User
from .models import User, Email_period, Category_Item, Notice, Notice_content
# Register your models here.
admin.site.register(User, UserAdmin)


#생성한 새로운 클래스의 데이터베이스를 여기다 저장해둔다. 
admin.site.register(Email_period)

# admin.site.register(Category)

admin.site.register(Category_Item)
admin.site.register(Notice)
admin.site.register(Notice_content)

#user model에 대한 추가 필드는 따로 admin페이지에 나타나지 않기 때문에 
#custom fields라는 섹션 아래 nickname field를 추가!
# UserAdmin.fieldsets += ("Custom fields", {"fields": ("nickname",)}  "department",  "phone" , "email_period", "is_active", "is_premier",)

UserAdmin.fieldsets +=(("Custom fields", {"fields": ("nickname", "department", "email_period", "category", "phone_number", )}),)


