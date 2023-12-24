from .models import UserReview
from rest_framework import serializers



class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserReview
        fields = ['name', 'email', 'message']

