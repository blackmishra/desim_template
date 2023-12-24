from django.db import models
from django.utils import timezone

class SubscribedUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField('Date Created', default=timezone.now())

    def __str__(self):
        return self.email
    

class UserReview(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message =  models.TextField()
    created_at = models.DateTimeField('Date Created', default=timezone.now())

    def __str__(self):
        return self.email