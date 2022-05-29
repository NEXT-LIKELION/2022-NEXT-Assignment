from django.shortcuts import render, redirect
from .models import Card, Groups, Friendlists
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import random
import qrcode
from PIL import Image
import os

# Create your views here.

    

def home(request):
    user = request.user
    if user.is_authenticated:
        card = Card.objects.get(owner=user)

        profile_pics = ['https://ifh.cc/g/lP9Q4y.png',
        'https://ifh.cc/g/DBKnAK.png',
        'https://ifh.cc/g/t5qXC4.png',
        'https://ifh.cc/g/86qcpa.png',
        'https://ifh.cc/g/3gGaD5.png',
        'https://ifh.cc/g/QxpyAj.png', 
        'https://ifh.cc/g/foD2kg.png',
        'https://ifh.cc/g/hLrAhp.png', 
        'https://ifh.cc/g/6tSO85.png',
        'https://ifh.cc/g/ql6ZkW.png', ]
    
        profile_pic = profile_pics[int(card.profile_pic)-1]

        return render(request, 'home.html', {
        'user':user,
        'card':card,
        'profile_pic': profile_pic
        })

    return render(request, 'home.html', {
        'user':user,
        })

def signup(request):
    # 프사 예시들
    profile_pics_1 = ['https://ifh.cc/g/lP9Q4y.png',
        'https://ifh.cc/g/DBKnAK.png',
        'https://ifh.cc/g/t5qXC4.png']
        
    profile_pics_2 = ['https://ifh.cc/g/86qcpa.png',
        'https://ifh.cc/g/3gGaD5.png',
        'https://ifh.cc/g/QxpyAj.png']
    
    profile_pics_3 = ['https://ifh.cc/g/foD2kg.png',
        'https://ifh.cc/g/hLrAhp.png', 
        'https://ifh.cc/g/6tSO85.png']
    profile_pics_4 = ['https://ifh.cc/g/ql6ZkW.png']

    if request.method == "POST":
        # 도메인을 벌써 소유한 다른 카드가 있는가?
        link = request.POST['link']
        found_link = Card.objects.filter(link = link)
        username = request.POST['username']
        password = request.POST['password1']
        found_user = User.objects.filter(username=username)

        if found_link:
            error = "같은 도메인의 소유자가 벌써 있습니다"
            return render(request, 'registration/signup.html', {
                'error': error,
                'profile_pics_1': profile_pics_1,
                'profile_pics_2': profile_pics_2,
                'profile_pics_3': profile_pics_3,
                'profile_pics_4': profile_pics_4
            })
        
        # 겹치는 아이디가 있는가?
        elif found_user:
            error = "이미 아이디가 존재합니다"
            return render(request, 'registration/signup.html', {
                'error': error,
                'profile_pics_1': profile_pics_1,
                'profile_pics_2': profile_pics_2,
                'profile_pics_3': profile_pics_3,
                'profile_pics_4': profile_pics_4
            })
        
        # 도메인&아이디가 배타적일 때 새 명함&계정 만들기

        new_user = User.objects.create_user(
            username = username,
            password = password,
        )

        auth.login(request,new_user)

        user = request.user
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        link = request.POST['link']
        intro = request.POST['intro']
        mbti = request.POST['mbti']
        profile_pic = request.POST['profile_pic']

        new_card = Card.objects.create(
            owner = user,
            link = link,
            name=name,
            phone_num=phone_num,
            intro=intro,
            mbti=mbti,
            profile_pic = profile_pic,
            )
        
        # 유저의 friendlist 만들기
        Friendlists.objects.create(
            me = user
        )
        return redirect('home')
    
    return render(request, 'registration/signup.html', {
        'profile_pics_1': profile_pics_1,
        'profile_pics_2': profile_pics_2,
        'profile_pics_3': profile_pics_3,
        'profile_pics_4': profile_pics_4
    })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(request.GET.get("next", "/"))
        error = "아이디와 비밀번호가 일치하지 않습니다"
        return render(request, 'registration/login.html', {
            'error': error,
        })
    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url="/registration/login")
def make(request):
    # 유저가 벌써 명함을 소유하고 있는가?
    user = request.user
    # if user.cards:
    #     error = "벌써 명함이 있습니다"
    #     return render(request, 'make.html', {'error':error})

    if request.method=="POST":
        name = request.POST['name']
        user = request.user
        phone_num = request.POST['phone_num']
        link = request.POST['link']
        intro = request.POST['intro']
        mbti = request.POST['mbti']

        # 도메인을 벌써 소유한 다른 카드가 있는가?
        already = Card.objects.filter(link = link)
        if len(already):
            error = "같은 도메인의 소유자가 벌써 있습니다"
            return render(request, 'make.html', {'error':error})
        else:
            new_card = Card.objects.create(
                owner = user,
                link = link,
                name=name,
                phone_num=phone_num,
                intro=intro,
                mbti=mbti,
                )
            return redirect('home')
    return render(request, "make.html")

@login_required(login_url="/registration/login")
def detail(request, card_link):
    user = request.user
    open_link = False
    # 1 대 1 초대
    if request.method == "POST":
        # 동일한 invitation_link를 가진 명함이 있는가?
        while True:
            new_code = random.randrange(0, 2000000000)
            already_card = Card.objects.filter(invitation_link = new_code)
            already_group = Groups.objects.filter(invitation_link = new_code)
            if not already_card and not already_group:
                break
            else:
                continue

        card = Card.objects.filter(link=card_link)

        card.update(
            invitation_link = new_code
        )
        return redirect('personal_invitation', card_link, new_code)
    
    card = Card.objects.get(link=card_link)

    profile_pics = ['https://ifh.cc/g/lP9Q4y.png',
        'https://ifh.cc/g/DBKnAK.png',
        'https://ifh.cc/g/t5qXC4.png',
        'https://ifh.cc/g/86qcpa.png',
        'https://ifh.cc/g/3gGaD5.png',
        'https://ifh.cc/g/QxpyAj.png', 
        'https://ifh.cc/g/foD2kg.png',
        'https://ifh.cc/g/hLrAhp.png', 
        'https://ifh.cc/g/6tSO85.png',
        'https://ifh.cc/g/ql6ZkW.png', ]
    profile_pic = profile_pics[int(card.profile_pic)-1]
    # 이 명함의 주인일 때
    if card.owner == user:
        # 명함의 링크가 열려있을 때
        if card.invitation_link:
            open_link = True
            return render(request, "detail.html",{
            'user':user,
            "open_link":open_link,
            "card":card,
            "profile_pic":profile_pic,
        })
        return render(request, "detail.html",{
            'user':user,
            "card":card,
            "profile_pic":profile_pic,
        })
    # 방문 유저와 명함이 같은 그룹에 있을 때
    user_groups = user.mygroups.all()
    access = False

    for group in user_groups:
        members = group.members.all()
        if card.owner in members:
            access = True
    
    # 방문 유저가 명함의 친구일 때

    friendlist = Friendlists.objects.get(me=user)
    if card.owner in friendlist.friends.all():
        access = True

    if access is True:
        return render(request, "detail.html", {
            'user':user,
            "card": card,
            "profile_pic":profile_pic,
            })

    # 열람 권한이 없을 때
    else:
        error = "이 명함의 열람 권한이 없습니다."
        return render(request, "detail.html", {"error":error})

#수정하기(혜영))
def edit(request, card_link):
    user = request.user
    card = Card.objects.get(link=card_link)
    if request.method == 'POST':
        link = request.POST['link']
        found_link = Card.objects.filter(link = link)
        

        if card.link == link:
            pass
        elif found_link:
            error = "같은 도메인의 소유자가 벌써 있습니다"
            return render(request, 'edit.html', {
                'error': error,
            })

        card = Card.objects.filter(link=card_link)

        card.update(
            name = request.POST['name'],
            owner = request.user,
            phone_num = request.POST['phone_num'],
            link = request.POST['link'],
            intro = request.POST['intro'],
            mbti = request.POST['mbti'],
            profile_pic = request.POST['profile_pic'],
        )
        return redirect('detail', link)

    profile_pics_1 = ['https://ifh.cc/g/lP9Q4y.png',
        'https://ifh.cc/g/DBKnAK.png',
        'https://ifh.cc/g/t5qXC4.png']
        
    profile_pics_2 = ['https://ifh.cc/g/86qcpa.png',
        'https://ifh.cc/g/3gGaD5.png',
        'https://ifh.cc/g/QxpyAj.png']
    
    profile_pics_3 = ['https://ifh.cc/g/foD2kg.png',
        'https://ifh.cc/g/hLrAhp.png', 
        'https://ifh.cc/g/6tSO85.png']

    profile_pics_4 = ['https://ifh.cc/g/ql6ZkW.png']

    card = Card.objects.get(link=card_link)
    return render(request, 'edit.html', {
        'card': card,
        'profile_pics_1': profile_pics_1,
        'profile_pics_2': profile_pics_2,
        'profile_pics_3': profile_pics_3,
        'profile_pics_4': profile_pics_4,
        })

@login_required(login_url="/registration/login")
def group_detail(request, group_pk):
    # 그룹장이 초대 링크 다시 열었을 때:
    # 동일한 invitation_link를 가진 그룹이 있는가?
    if request.method == "POST":
        while True:
                new_code = random.randrange(0, 2000000000)
                already_group = Groups.objects.filter(invitation_link = new_code)
                already_card = Card.objects.filter(invitation_link = new_code)
                if not already_group and not already_card:
                    break
                else:
                    continue
        group = Groups.objects.filter(pk=group_pk)
        group.update(
            invitation_link=new_code
        )
        group = Groups.objects.get(pk=group_pk)
        return redirect('group_invitation', group.pk, new_code)
    group = Groups.objects.get(pk=group_pk)
    user = request.user
    members = group.members.all()
    member_card = []
    open_link = False
    is_creater = False
    for member in members:
        card = Card.objects.get(owner = member)
        member_card.append(card)
    # 링크가 열려있는 그룹 + 그룹장이 열었을 때
    if group.invitation_link and user == group.creater:
        open_link = True
        return render(request, "group_detail.html", {
            'open_link': open_link,
            'group': group,
            'user':user,
            'members': members,
            'member_card': member_card
        })
    # 링크가 닫혀있고 + 그룹장이 열었을 때
    if user == group.creater:
        is_creater = True
        return render(request, "group_detail.html", {
            'is_creater': is_creater,
            'group': group,
            'user':user,
            'members': members,
            'member_card': member_card
        })
    # 그룹 맴버가 열었을 때
    if user in members:
        return render(request, "group_detail.html", {
            'open_link': open_link,
            'group': group,
            'user':user,
            'members': members,
            'member_card': member_card
        })
    else:
        error = "이 그룹의 열람 권한이 없습니다."
        return render(request, "group_detail.html", {
            'error': error
        })

@login_required(login_url="/registration/login")
def group_list(request, card_link):
    user = request.user
    groups = user.mygroups.all()
    card = Card.objects.get(link=card_link)
    # 이 명함의 주인일 때
    if card.owner == user:
        return render(request, "group_list.html",{
            "card":card,
            'user':user,
            'groups':groups,
        })
    else:
        error = "이 명함 그룹의 열람 권한이 없습니다."
        return render(request, "group_list.html",{
            "error": error,
            "card":card,
            'user':user,
            'groups':groups,
        })

@login_required(login_url="/registration/login")
def make_group(request):
    if request.method == "POST":
        name = request.POST["name"]

        # 동일한 invitation_link를 가진 그룹이 있는가?
        while True:
            new_code = random.randrange(0, 2000000000)
            already_group = Groups.objects.filter(invitation_link = new_code)
            already_card = Card.objects.filter(invitation_link = new_code)
            if not already_group and not already_card:
                break
            else:
                continue

        new_group = Groups.objects.create(
            name=name,
            creater=request.user,
            invitation_link=new_code
            )
        return redirect('group_invitation', new_group.pk, new_code)
    return render(request, "make_group.html")

@login_required(login_url="/registration/login")
def group_invitation(request, group_pk, access_code):
    group = Groups.objects.get(pk=group_pk)
    user = request.user
    # 코드가 유효하면, 사이트에 입장한 유저 그룹 멤버에 추가하기
    if group.invitation_link == access_code:
        group.members.add(user)
        group.save()
    else:
        error = "이 그룹의 초대 코드가 사라졌습니다. 그룹장에게 문의해 주세요."
        owner_name = Card.objects.get(owner=group.creater).name
        return render(request, "group_invitation.html", {
        'owner_name': owner_name,
        'user': user,
        'group': group,
        'error': error
    })

    # 관리자가 QR코드 닫기 버튼 눌렀을 때, 공유 링크 닫기
    if request.method == "POST":
        group = Groups.objects.filter(pk=group_pk)
        group.update(invitation_link=None)
        group = Groups.objects.get(pk=group_pk)
        return redirect("group_detail", group_pk)

    # qr 코드 생성하여 띄우기

    img = qrcode.make('group/'+ str(group_pk)+'/'+ str(access_code)+'/')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data('group/'+str(group_pk)+'/'+str(access_code)+'/')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img_path = "./mainApp/static/qr_codes/"

    img.save(img_path + str(access_code) + ".png")
    qrcode_pic_route = "qr_codes/"+str(access_code)
    return render(request, "group_invitation.html", {
        'user': user,
        'group': group,
        'img': img,
        'img_path': img_path,
        'qrcode_pic_route':qrcode_pic_route,
    })

@login_required(login_url="/registration/login")
def personal_invitation(request, card_link, access_code):
    guest = request.user
    card = Card.objects.get(link=card_link)
    card_owner = card.owner
    ownerlist = Friendlists.objects.get(me = card_owner)
    guestlist = Friendlists.objects.get(me = guest)


    # 코드가 유효하면, 사이트에 입장한 유저 친구 추가하기 (유저가 카드 주인이 아닐 경우)
    if card.invitation_link == access_code:
        if guest == card.owner:
            pass
        else:
            ownerlist.friends.add(guest)
            ownerlist.save()
            guestlist.friends.add(card_owner)
            guestlist.save()
            return render(request, 'personal_invitation.html', {
                'card': card,
                'guest': guest,
                'card_owner': card_owner
            })
    else:
        error = "이 명함의 공유 코드가 닫혔습니다. 명함 주인에게 문의해주세요."
        return render(request, "personal_invitation.html", {
        'error': error,
        'card': card,
        'guest': guest,
        'card_owner': card_owner
    })

    # 관리자가 QR코드 닫기 버튼 눌렀을 때, 공유 링크 닫기
    if request.method == "POST":
        card = Card.objects.filter(link=card_link)
        card.update(invitation_link=None)
        card = Card.objects.get(link=card_link)
        return redirect("detail", card_link)

    # qr 코드 생성하여 띄우기
    img_path = "./mainApp/static/qr_codes/"
    img = qrcode.make(str(card.link)+'/'+ str(access_code))
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(str(card.link)+'/'+ str(access_code))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
   

    img.save(img_path + str(access_code) + ".png")
    
    qrcode_pic_route = "qr_codes/"+str(access_code)
    return render(request, 'personal_invitation.html',{
        'qrcode_pic_route': qrcode_pic_route,
        'card': card,
        'guest': guest,
        'card_owner': card_owner
        })

@login_required(login_url="/registration/login")
def friend_list(request, card_link):
    user = request.user
    card = Card.objects.get(link=card_link)
    # 이 명함의 주인일 때
    if card.owner != user:
        error = "이 친구 목록의 열람 권한이 없습니다."
        return render(request, "friend_list.html", {
            'error': error
        })
    else:
        groups = user.mygroups.all()
        all_cards_list = []
        all_link_list = []

        # 카드의 모든 그룹에 있는 멤버들 전부 뽑아오기
        for group in groups:
            members = group.members.all()
            for member in members:
                friend_card = Card.objects.get(owner=member)
                if friend_card == card:
                    pass
                else:
                    all_cards_list.append([str(friend_card.name), str(friend_card.phone_num)])
                    all_link_list.append(str(friend_card.link))
        
        # 카드의 친구들 전부 뽑아오기
        friendlist = Friendlists.objects.get(me=user)
        for friend in friendlist.friends.all():
            friend_card = Card.objects.get(owner=friend)
            all_cards_list.append([str(friend_card.name), str(friend_card.phone_num)])
            all_link_list.append(str(friend_card.link))

        # 중복 제외
        all_cards_list_new = []
        for item in all_cards_list:
            if item not in all_cards_list_new:
                all_cards_list_new.append(item)

        all_link_list_new = []
        for item in all_link_list:
            if item not in all_link_list_new:
                all_link_list_new.append(item)
        
        # 이 명함의 주인일 때
        if card.owner == user:
            return render(request, "friend_list.html",{
                "card":card,
                'user':user,
                'groups':groups,
                'all_cards_list_new': all_cards_list_new,
                'all_link_list_new':all_link_list_new,
            })
        else:
            error = "이 명함 그룹의 열람 권한이 없습니다."
            return render(request, "friend_list.html",{
                "error": error,
                "card":card,
                'user':user,
                'groups':groups,
            })
