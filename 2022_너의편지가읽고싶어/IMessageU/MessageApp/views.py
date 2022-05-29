from turtle import left, update
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from LoginApp.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html')


def my_page(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        if request.user.pk == user_pk:
            update_user = User.objects.get(pk=user_pk)
            update_message = Message.objects.filter(receiver = user)
            for message in update_message:
              message.left_time -= int(request.POST['totaltime'])
              message.minute = int(message.left_time/60)
              message.second = message.left_time%60
              message.save()
            if update_user.total_time == None:
              update_user.total_time = int(request.POST['totaltime'])
              update_user.save(update_fields=['total_time'])
              return redirect('my_page', user_pk)
            else:
              added_time = update_user.total_time + int(request.POST['totaltime'])
              update_user.total_time += int(request.POST['totaltime'])
              update_user.save()
              return redirect('my_page', user_pk)
        new_message = Message.objects.create(
          sender=request.user,
          receiver=user,
          title=request.POST['title'],
          content=request.POST['content'],
          message_cover = request.POST['message_cover'],
          left_time = request.POST['left_time'],
          nickname = request.POST['nickname'],
          minute = int(request.POST['left_time'])/60,
          second = int(request.POST['left_time'])%60,
    )
        
        return redirect('message_detail', new_message.pk)

    isHost = True
    print(isHost, 'true')
    if (request.user.pk != user_pk):
        isHost = False
        print('false')

    messages = Message.objects.filter(receiver=user)
    print('1')
    len_message = len(messages)
    print('len')

    return render(request, 'my_page.html', {'messages': messages, 'isHost': isHost, 'len_message': len_message,})
    

def message_detail(request, message_pk):
    messages = Message.objects.get(pk=message_pk)

    return render(request, 'message_detail.html', {'messages': messages})
