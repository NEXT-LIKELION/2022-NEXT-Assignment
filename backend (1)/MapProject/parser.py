import json

import sys,io,os
import django

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MapProject.settings")
django.setup()

from .models import School


def parsing():

    with open('school.json') as json_file:
        json_data = json.load(json_file)

    post = []

    for i in range(12):
        post.append({
            'name': json_data['schools'][i]['name'],
            'loc': json_data['schools'][i]['loc'],
            'lat': json_data['schools'][i]['lat'],
            'lon': json_data['schools'][i]['lon']
        })

    return post


if __name__ == '__main__':
    post = parsing()

    for i in range(len(post)):
        School(
            name=post[i]['name'],
            location=post[i]['loc'],
            latitude=post[i]['lat'],
            longitude=post[i]['lon']
        ).save()