from django.shortcuts import render, redirect
from .models import User, Test, Guest


def main(request):
    return render(request, 'main.html')
    
# Create your views here.
def user_create(request):
    if (request.method=="POST"):
        user= User.objects.create(
            name = request.POST['username'],
        )
        return redirect('testcreate', user.pk)
    
        # return render(request, 'user1_create.html', {'user':user})
    
    return render(request, 'user1_login.html')


def test_create(request, user_pk):
    userObj = User.objects.get(pk=user_pk)
    if (request.method == "POST"):
        
        new_test = Test.objects.create(
            username = userObj,
            testname = request.POST['testname'],

            truetag1=request.POST['truelike1'],
            truetag2=request.POST['truelike2'],
            truetag3=request.POST['truelike3'],
            truetag4=request.POST['truelike4'],
            truetag5=request.POST['truelike5'],
            
            falsetag1=request.POST['falselike1'],
            falsetag2=request.POST['falselike2'],
            falsetag3=request.POST['falselike3'],
            falsetag4=request.POST['falselike4'],
            falsetag5=request.POST['falselike5'],
        )
        return redirect('testcheck', new_test.pk)
    
    return render(request, 'user1_create.html', {'user':userObj})

def test_checksend(request, test_pk):
    test = Test.objects.get(pk=test_pk)

    # link share fuction

    return render(request, 'user1_check.html', {'test':test})

# share lobby
def lobby(request, test_pk):
    test = Test.objects.get(pk=test_pk)

    return render(request, 'user12lobby.html', {'test':test})

# Guest
def guest_create(request, test_pk):
    test = Test.objects.get(pk=test_pk)
    if request.method == "POST":
        new_guest = Guest.objects.create(
            name = request.POST["guestname"]
            )
        return redirect('dotest', test.pk, new_guest.pk)
    return render(request, 'user2_login.html', {'test':test})
    

def test_load(request, test_pk, guest_pk):
    test = Test.objects.get(pk=test_pk)
    guest = Guest.objects.get(pk=guest_pk)
    truetag = [test.truetag1, test.truetag2,
               test.truetag3, test.truetag4, test.truetag5]
    

    # get guest's answer
    # guestObj = Guest.objects.get(pk=guest_pk)
    # if request.method=="POST":
    #     guest_test = Test.objects.create(
    #         username = guestObj,
    #         testname = test.name,

    #         truetag1 = request.POST['sel1'],
    #         truetag2 = request.POST['sel2'],
    #         truetag3 = request.POST['sel3'],
    #         truetag4 = request.POST['sel4'],
    #         truetag5 = request.POST['sel5'],
    #         falsetag1 = '',
    #         falsetag2 = '',
    #         falsetag3 = '',
    #         falsetag4 = '',
    #         falsetag5 = '',
    #     )
    #     return redirect('result', test_pk, guest_test.pk)

    return render(request, 'user2_test.html', {'test': test, 'guest':guest, 'truetag':truetag,})


def test_result(request, test_pk, guest_pk): # , gtest_pk
    test = Test.objects.get(pk=test_pk)
    guest = Guest.objects.get(pk=guest_pk)
    # gtest = Test.objects.get(pk=gtest_pk)
    # result = 0
    truetag = [test.truetag1, test.truetag2,
                   test.truetag3, test.truetag4, test.truetag5]
    # if gtest.truetag1 in truetag:
    #     result += 1
    # if gtest.truetag2 in truetag:
    #     result += 1
    # if gtest.truetag3 in truetag:
    #     result += 1
    # if gtest.truetag4 in truetag:
    #     result += 1
    # if gtest.truetag5 in truetag:
    #     result += 1

    #result -> differnt page
    # if result == 0:
    #     return render(request, '')
    # elif result == 1:
    #     return render(request, '')
    # elif result == 2:
    #     return render(request, '')
    # elif result == 3:
    #     return render(request, '')
    # elif result == 4:
    #     return render(request, '')
    # elif result == 5:
    #     return render(request, '')
        

    return render(request, 'result.html', {'test':test, 'guest':guest, }) #'result':result

def test_final(request, number):

    if number==1:
        return render(request, 'result1.html')
    elif number==2:
        return render(request, 'result2.html')
    elif number == 3:
        return render(request, 'result3.html')
    elif number == 4:
        return render(request, 'result4.html')
    elif number == 5:
        return render(request, 'result5.html')
    elif number == 6:
        return render(request, 'result6.html')
    pass