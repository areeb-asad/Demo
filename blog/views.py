from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import post

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_post'

    def get_queryset(self):
        """Return the last five published questions."""

        return post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = post
    template_name = 'blog/detail.html'