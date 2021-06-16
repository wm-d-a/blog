from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', post_new, name='post_new'),
]
