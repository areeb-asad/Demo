from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import post
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_post'

    def get_queryset(self):
        """Return the last five published questions."""

        return post.objects.filter(is_published=True).order_by('-pub_date')[:5]



class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be viewed or edited.
    """
    queryset = post.objects.order_by('-pub_date')[:5]
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class DetailView(generic.DetailView):
    model = post
    template_name = 'blog/detail.html'