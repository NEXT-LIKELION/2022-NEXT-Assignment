from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now


# Create your models here.

class Emotion(models.Model):
    
    status = models.CharField(max_length=1)
    emoji = models.ImageField(upload_to="emoji/")

    def __str__(self):
        return self.status

# 동물 프로필 이미지 저장 경로 설정
def profile_directory_path(owner, filename):
    # file will be uploaded to MEDIA_ROOT/post/user_<id>/<filename>
    return 'pet_profile/user_{0}/{1}'.format(owner.id, filename)

class Pet(models.Model):
    SPECIES = (
        ('D', 'dog'),
        ('C', 'cat')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    species = models.CharField(max_length=1, choices=SPECIES)
    name = models.CharField(max_length=50)
    profile_img = models.ImageField(blank=True, null=True)
    birth = models.DateField(default=now)
    introduction = models.CharField(max_length=100, default="")

    class Meta:
        unique_together = (('owner', 'name'))

    def __str__(self):
        return self.name

# 자주 기록하는 할 일 태그로 등록
class Tag(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Todo(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    date = models.DateField(default=now)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="todos")
    


# 일기 사진 저장 경로 설정
def photo_directory_path(writer, filename):
    # file will be uploaded to MEDIA_ROOT/post/user_<id>/<filename>
    return 'diary/user_{0}/{1}'.format(writer.pk, filename)


class Diary(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name="posts")
    uploaded = models.DateField(default=now)
    photo = models.ImageField(blank=True, null=True)
    content = models.TextField(max_length=100)

# Post 모델은 추후에 구현(우선 건드리지 맙시다)
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(upload_to="post/%Y/%m/%d/", null=True, blank=True)
    uploaded = models.DateField(auto_now_add=True)

# Post 모델 구현할 때 같이 구현
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=50)
    uploaded = models.DateField(auto_now_add=True)

