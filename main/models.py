from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    GOAL_CATEGORY_CHOICES = [
        ('study', 'study'),
        ('hobby', 'hobby'),
        ('etc', 'etc'),
    ]
    CERTIFY_CATEGORY_CHOICES = [
        ('image', 'image'),
        ('text', 'text'),
        ('figure', 'figure'),
    ]
    category = models.CharField(choices=GOAL_CATEGORY_CHOICES, max_length=50)   # 카테고리(공부, 취미, 기타)
    certify_method = models.CharField(choices=CERTIFY_CATEGORY_CHOICES, max_length=50)      # 인증 방식(이미지, 글, 수치)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)     # 목표 작성자 = 매니저
    name = models.CharField(max_length=100)     # 목표 이름
    description = models.TextField()    # 목표 설명
    created = models.DateField()    # 목표 글 작성 날짜
    start_date = models.DateField()     # 목표 시행 날짜
    fee = models.IntegerField(default=500)      # 참가비
    value = models.IntegerField(null=True, blank=True)     # 인증 방식이 수치인 경우만
    unit = models.CharField(max_length=10, null=True, blank=True)     # 인증 방식이 수치인 경우만
    criteria = models.BooleanField(default=True)    # 인증 방식이 수치인 경우만. true면 이상, false면 이하로 처리
    member = models.ManyToManyField(User, related_name='members')    # 참여 인원
