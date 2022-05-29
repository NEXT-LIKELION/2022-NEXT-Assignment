from django.contrib import admin
from django.urls import path, include
from MessageApp import views
from LoginApp.views import login, logout, signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #메인화면
    path('', views.home, name='home'), 
    
    #회원가입, 로그인, 로그아웃 화면
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('allauth.urls')),

    #메시지 관련 화면
    path('my_page/<int:user_pk>', views.my_page, name='my_page'),
    path('my_page/message_detail/<int:message_pk>', views.message_detail, name='message_detail'),
]
