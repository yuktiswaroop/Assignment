from django.contrib import admin
from django.urls import path
from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,UserPostList
from . import views

urlpatterns = [
    path('', PostList.as_view() , name ='home'),
    path('user/<str:username>', UserPostList.as_view() , name ='user-posts'),
    path('post/<int:pk>/', PostDetail.as_view() , name ='post-detail'),
    path('post/new/', PostCreate.as_view() , name ='post-create'),
    path('post/<int:pk>/update/', PostUpdate.as_view() , name ='post-update'),
    path('post/<int:pk>/delete/', PostDelete.as_view() , name ='post-delete'),
    path('about/', views.about , name ='blog-about'),

]


 