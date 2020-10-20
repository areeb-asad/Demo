from rest_framework import serializers
from .models import post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = post
        fields = ['title', 'pub_date','content','id']