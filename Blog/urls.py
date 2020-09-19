
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home,name='blog-name'),
    path('create', views.PostFormView,name='PostFormView'),
    path('about/', views.About,name='blog-about'),
    path('like/', views.Like_Post,name='like_post'),
    path('detail/<int:id>', views.Post_Detail_View,name='post_detail')
    ]
