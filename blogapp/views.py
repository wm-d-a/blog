from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import PostForm
from .models import *


def index(request):
    posts = Post.objects.all()
    rubrics = Rubric.objects.all()
    context = {'posts': posts, 'rubrics': rubrics}
    return render(request, 'blogapp/main_page.html', context)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blogapp/post.html'
    context_object_name = 'post'


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogapp/PostForm.html', {'form': form})
