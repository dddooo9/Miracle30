from django.db import models
from django.contrib.auth.models import User
from main.models import Goal


class CertifyImage(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()
    image = models.ImageField(upload_to='certify_image/')
    achievement = models.BooleanField(default=False)


class CertifyText(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='texts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()
    text = models.TextField()
    achievement = models.BooleanField(default=False)


class CertifyFigure(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='figures')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()
    figure = models.IntegerField()
    achievement = models.BooleanField(default=False)
