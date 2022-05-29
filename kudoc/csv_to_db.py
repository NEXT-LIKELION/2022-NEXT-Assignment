import sys
import csv
import os

from datetime import date
# from appAccount.models import Category_Item
# from appAccount.models import Notice
# 환경 변수 설정
# sys.path.append("/Users/baegmingi/Desktop/일기/Hackathon_Mut4Joa/kudoc")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kudoc.settings")
import django
# django.setup()


# print(date.today())

# mainApp 폴더에 존재하는 models.py에서 Building 모델을 불러온다

# categorys_items = Category_Item.objects.all()


# print(categorys_items)

# print(categorys_items[0])

# 통계학과 링크
depart_link = "https://portal.korea.ac.kr/front/Intro.kpd"

with open('/Users/baegmingi/Desktop/일기/Hackathon_Mut4Joa/kudoc/portalnotice.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # row[0] 이것은 타이틀입니다.
        # row[1] 이것은 링크입니다.  depart_link + row[1]
        # 통계학과의 경우 앞에 https://stat.korea.ac.kr/stat/community/notice_under.do 이것을 붙여줍니다.
        # row[2] 이것은 날짜입니다. 형식은 2018.01.12
        # date = row[2].replace('.', '-')
        # dateformat = '%Y-%m-%d'
        # str_datetime = '2021-07-18 12:15:33'
        # str_datetime = str(row[2].replace('.', '-')) + ' 12:15:33'
        # dateformat = '%Y-%m-%d %H:%M:%S'
        # newDate = datetime.strptime(str_datetime, dateformat)
        # print(str_datetime)

        depart_name = row[3].strip('<i>')
        depart_name = depart_name.rstrip('</')
        print(row[0])
        # print(row[1])
        # print(row[2])

        # pk_num = 0

        # for i in categorys_items:
        #     if(i.item == depart_name):
        #         pk_num = i.pk

        # print(pk_num)

        # category = Category_Item.objects.get(pk=9)
        # print(type(category))

        # category_depart = categorys_items.get(pk=1)
        # print(category_depart)
        # row[3] 이것은 학과명입니다.
        # print(row[3])
        # print(date)

        # Category_Item.objects.filter('')

        # _, created = Notice.objects.get_or_create(
        #     title=row[0],
        #     link=depart_link + row[1],
        #     # category = category,
        #     # post_date = date.today(),
        # )
