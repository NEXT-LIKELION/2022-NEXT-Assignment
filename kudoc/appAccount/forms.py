from django import forms
from .models import User, Email_period, Category_Item

#('기억하기 위한 것', '들어가야하는 내용')
# choices = [('1일', '1일'), ('3일', '3일'), ('7일', '7일'), ('14일', '14일'), ('30일', '30일')]

# 하나하나 적는 것 대신에 쿼리를 가져오기
choices = Email_period.objects.all().values_list('period', 'period')
items = Category_Item.objects.all().values_list('item', 'item')
# modles from은 사용할 모델을 만들면, 모델에 따라서 다르게 만드는 것이다.




class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        # 추가해준 필드만 가져오면 됨.
        fields = ("nickname", "department", "phone_number", "email_period", "category",)

        widgets = {
            # 'email_period': forms.Select(choices=choices, attrs={'class':'form-control'}),
            # 'email_period': forms.Select(choices=choices, attrs={'class':'form-control', placeholder로 뭐나오는지보기}),
            'email_period': forms.Select(choices=choices, attrs={'class':'form-control'}),
            'category': forms.Select(choices=items, attrs={'class':'form-control'}),
        }

        # form을 보여주는 방식
    def signup(self, request, user):
        # form이 기입된 데이터는 cleaned_data로 가져올 수 있다.
        user.nickname = self.cleaned_data['nickname']
        user.category = self.cleaned_data['category']
        user.phone_number = self.cleaned_data['phone_number']
        user.department = self.cleaned_data['department']
        user.email_period = self.cleaned_data['email_period']
        user.save()


'''

        widgets = {
            # 'email_period': forms.Select(choices=choices, attrs={'class':'form-control'}),
            # 'email_period': forms.Select(choices=choices, attrs={'class':'form-control', placeholder로 뭐나오는지보기}),
            'email_period': forms.Select(choices=choices, attrs={'class':'form-control'}), 
            # 'category': forms.Select(choices=items, attrs={'class':'form-control'}),
        }
'''
