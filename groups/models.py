from django.db import models
from django.contrib.auth.models import User
from main.models import Goal


class Certify(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='certifies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()
    image = models.ImageField(upload_to='certify_image/', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    figure = models.FloatField(null=True, blank=True)
    achievement = models.BooleanField(default=True)
    