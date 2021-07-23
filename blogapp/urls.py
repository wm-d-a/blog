from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post'),
    path('post/new/', NewPost.as_view(), name='post_new'),
    path('rubric/<int:pk>/', RubricView.as_view(), name='rubricView')
]

# urlpatterns = [
#     path('', index, name='index')
#     path('post/<int:post_id>/', postDetail, name='post'),
#     path('post/new/', post_new, name='post_new'),
#     path('rubric/<int:rubric_id>/', rubricView, name='rubricView')
# ] Для контроллеров-функций
