from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic.edit import UpdateView
from .forms import PostForm
from .models import *


class MainPage(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blogapp/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class RubricView(ListView):
    template_name = 'blogapp/rubric.html'

    # context_object_name = 'rubric'

    def get_queryset(self):
        return Post.objects.filter(rubric=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r = Rubric.objects.get(pk=self.kwargs['pk'])
        context['rubric'] = r
        context['posts'] = r.post_set.all()
        return context


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blogapp/post.html'
    context_object_name = 'post'  # в это значение будет сохранена полученная запись


class NewPost(FormView):
    template_name = 'blogapp/PostForm.html'
    form_class = PostForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('rubricView', kwargs={'pk': self.object.cleaned_data['rubric'].pk})


class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    template_name = 'blogapp/PostEdit.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('post', pk=post.pk)
#     else:
#         form = PostForm()
#         return render(request, 'blogapp/PostForm.html', {'form': form})

# def rubricView(request, rubric_id):
#     r = Rubric.objects.get(pk=rubric_id)
#     posts = r.post_set.all()
#     context = {'posts': posts, 'rubric': r}
#     return render(request, 'blogapp/rubric.html', context)

# def postDetail(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = {'post': post}
#     return render(request, 'blogapp/post.html', context)


# def index(request):
#     posts = Post.objects.all()
#     rubrics = Rubric.objects.all()
#     context = {'posts': posts, 'rubrics': rubrics}
#     return render(request, 'blogapp/main_page.html', context)
