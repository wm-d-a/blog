from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *


def index(request):
    posts = Post.objects.all()
    rubrics = Rubric.objects.all()
    context = {'posts': posts, 'rubrics': rubrics}
    return render(request, 'blogapp/main_page.html', context)


# def post(request):
#     posts = Post.objects.all()
#     context = {'post': posts}
#     return render(request, 'blogapp/post.html', context)
